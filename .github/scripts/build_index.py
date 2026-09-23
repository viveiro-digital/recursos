"""Validate resource entries and rebuild the README index from their frontmatter.

Categories and their display names come from .portal/config.json, in the order
listed there. The index is written between the INDEX_START and INDEX_END
markers in README.md.

Validation runs first. If any entry is invalid, every problem is reported and
the script exits with status 1 without touching README.md.

Messages are in Portuguese because they are shown to contributors.

Usage:
    python3 .github/scripts/build_index.py
    python3 .github/scripts/build_index.py --check
    python3 .github/scripts/build_index.py --report report.md --note "text"

Options:
    --check          Validate only; fail if the README index is outdated.
    --report PATH    Write a Markdown report (problems and index changes),
                     used for the job summary and the pull request comment.
    --note TEXT      Extra line appended to the report.
"""

import argparse
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
CONFIG = ROOT / ".portal" / "config.json"
INDEX_START = "<!-- indice:inicio -->"
INDEX_END = "<!-- indice:fim -->"
REPORT_MARKER = "<!-- index-report -->"

ALLOWED_TYPES = {
    "ferramenta", "guia", "padrão", "política", "publicação",
    "legislação", "iniciativa", "comunidade", "acervo",
}
FILENAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")
FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.S)
SOURCE_PATTERN = re.compile(r"^\[Fonte oficial\]\((\S+?)\)$")
INDEX_LINE_PATTERN = re.compile(r"^- \[(.+?)\]\(([^)]+\.md)\): ")
# Files at the repository root that are not entries.
ROOT_FILES = {"README.md", "CONTRIBUTING.md", "AGENTS.md", "CLAUDE.md"}

errors = []


def error(path, message):
    errors.append((path.relative_to(ROOT).as_posix(), message))


def parse_value(raw):
    raw = raw.strip()
    if raw.startswith('"'):
        return json.loads(raw)
    return raw


def normalize(text):
    """Lowercase and strip accents, so near-identical titles collide."""
    decomposed = unicodedata.normalize("NFKD", text.casefold())
    return "".join(c for c in decomposed if not unicodedata.combining(c)).strip()


def normalize_url(url):
    return re.sub(r"^https?://(www\.)?", "", url).rstrip("/").casefold()


def read_entry(path, folder):
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        error(path, "cabeçalho (frontmatter) ausente; o arquivo deve começar com um bloco ---")
        return None

    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            try:
                fields[key.strip()] = parse_value(value)
            except json.JSONDecodeError:
                error(path, f"valor entre aspas inválido no campo `{key.strip()}`")

    for name in ("title", "description", "type", "tags"):
        if not fields.get(name):
            error(path, f"campo `{name}` ausente ou vazio")

    title = fields.get("title", "")
    description = fields.get("description", "")
    if title and description and normalize(description).rstrip(".") == normalize(title):
        error(path, "`description` repete o título; descreva o que o recurso é")
    if description and not description.endswith("."):
        error(path, "`description` deve terminar com ponto final")

    entry_type = fields.get("type")
    if entry_type and entry_type not in ALLOWED_TYPES:
        allowed = ", ".join(sorted(ALLOWED_TYPES))
        error(path, f"`type` inválido: `{entry_type}`; valores aceitos: {allowed}")

    tags = fields.get("tags", "")
    if tags and folder not in re.findall(r"[\w-]+", tags):
        error(path, f"`tags` deve incluir a pasta da categoria, `{folder}`")

    body = text[match.end():].lstrip("\n")
    first_line = body.split("\n", 1)[0].strip()
    source = SOURCE_PATTERN.match(first_line)
    if not source:
        error(path, "a primeira linha depois do cabeçalho deve ser `[Fonte oficial](<link>)`")

    return {
        "path": path,
        "folder": folder,
        "title": title,
        "description": description,
        "source": source.group(1) if source else None,
    }


def collect_entries(categories):
    entries = []

    for folder in categories:
        if not (ROOT / folder).is_dir():
            error(CONFIG, f"a categoria `{folder}` está registrada, mas a pasta não existe")

    for directory in sorted(p for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith(".")):
        markdown_files = sorted(directory.rglob("*.md"))
        if directory.name not in categories:
            for path in markdown_files:
                error(path, f"a pasta `{directory.name}` não está registrada como categoria em `.portal/config.json`")
            continue
        for path in markdown_files:
            if path.parent != directory:
                error(path, "entradas ficam direto na pasta da categoria, sem subpastas")
                continue
            if not FILENAME_PATTERN.match(path.name):
                error(path, "nome de arquivo deve ter só minúsculas sem acento, números e hífens")
            entry = read_entry(path, directory.name)
            if entry:
                entries.append(entry)

    for path in sorted(ROOT.glob("*.md")):
        if path.name not in ROOT_FILES:
            error(path, "entradas ficam dentro da pasta de uma categoria")

    return entries


def check_duplicates(entries):
    for key, label, normalizer in (
        ("title", "título", normalize),
        ("source", "link da fonte oficial", normalize_url),
    ):
        seen = {}
        for entry in entries:
            if not entry[key]:
                continue
            value = normalizer(entry[key])
            if value in seen:
                first = seen[value]["path"]
                error(entry["path"], f"{label} duplicado: igual ao de `{first.relative_to(ROOT).as_posix()}`")
                error(first, f"{label} duplicado: igual ao de `{entry['path'].relative_to(ROOT).as_posix()}`")
            else:
                seen[value] = entry


def render_index(categories, entries):
    sections = []
    for folder, name in categories.items():
        items = sorted(
            (e for e in entries if e["folder"] == folder),
            key=lambda e: normalize(e["title"]),
        )
        if not items:
            continue
        lines = "\n".join(
            f"- [{e['title']}]({folder}/{e['path'].name}): "
            f"{e['description'][0].lower()}{e['description'][1:]}"
            for e in items
        )
        sections.append(f"### {name}\n\n{lines}")
    return "\n\n".join(sections)


def split_readme(readme):
    """Return (before, index, after), or None if the markers are wrong."""
    if readme.count(INDEX_START) != 1 or readme.count(INDEX_END) != 1:
        error(README, f"o README deve conter `{INDEX_START}` e `{INDEX_END}` uma vez cada")
        return None
    before, rest = readme.split(INDEX_START)
    index, after = rest.split(INDEX_END)
    return before, index, after


def index_lines(index):
    """Map each entry path in an index to its (title, full line)."""
    lines = {}
    for line in index.splitlines():
        match = INDEX_LINE_PATTERN.match(line)
        if match:
            lines[match.group(2)] = (match.group(1), line)
    return lines


def index_changes(old_index, new_index):
    old, new = index_lines(old_index), index_lines(new_index)
    added = [(new[p][0], p) for p in new if p not in old]
    removed = [(old[p][0], p) for p in old if p not in new]
    changed = [(new[p][0], p) for p in new if p in old and old[p][1] != new[p][1]]
    return added, changed, removed


def repo_url():
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    repository = os.environ.get("GITHUB_REPOSITORY", "viveiro-digital/recursos")
    return f"{server}/{repository}"


def write_report(path, entries, changes, note):
    lines = [REPORT_MARKER, "## Validação das entradas", ""]
    if errors:
        lines.append(f"**Resultado:** {len(errors)} problema(s) encontrado(s). O índice não foi atualizado.")
        lines.append("")
        lines += [f"- `{file}`: {message}" for file, message in errors]
        lines += ["", f"Corrija os problemas e envie um novo commit. As regras estão em [CONTRIBUTING.md]({repo_url()}/blob/main/CONTRIBUTING.md)."]
    else:
        lines.append(f"**Resultado:** as {len(entries)} entradas são válidas.")
        lines += ["", "### Mudanças no índice", ""]
        added, changed, removed = changes
        if not (added or changed or removed):
            lines.append("Nenhuma mudança no índice.")
        for label, items in (("Adicionada", added), ("Alterada", changed), ("Removida", removed)):
            lines += [f"- {label}: {title} (`{entry}`)" for title, entry in items]
    if note and not errors:
        lines += ["", note]
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_errors():
    in_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    for path, message in errors:
        if in_actions:
            print(f"::error file={path}::{message}")
        else:
            print(f"{path}: {message}", file=sys.stderr)
    print(f"\n{len(errors)} problema(s) encontrado(s). O README não foi alterado.", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Validate entries and rebuild the README index.")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--report")
    parser.add_argument("--note", default="")
    args = parser.parse_args()

    categories = json.loads(CONFIG.read_text(encoding="utf-8"))["navigation"]["labelOverrides"]
    entries = collect_entries(categories)
    check_duplicates(entries)

    readme = README.read_text(encoding="utf-8")
    parts = split_readme(readme)
    new_index = render_index(categories, entries)
    changes = index_changes(parts[1], new_index) if parts else ([], [], [])

    if args.report:
        write_report(args.report, entries, changes, args.note)

    if errors:
        print_errors()
        sys.exit(1)

    before, _, after = parts
    updated = f"{before}{INDEX_START}\n\n{new_index}\n\n{INDEX_END}{after}"
    if updated == readme:
        print(f"O índice está atualizado ({len(entries)} entradas).")
    elif args.check:
        print("O índice do README está desatualizado. Execute: python3 .github/scripts/build_index.py", file=sys.stderr)
        sys.exit(1)
    else:
        README.write_text(updated, encoding="utf-8")
        print(f"Índice gerado ({len(entries)} entradas).")


if __name__ == "__main__":
    main()
