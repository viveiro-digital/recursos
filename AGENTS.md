# Instruções para agentes

Antes de criar ou editar qualquer texto deste repositório (entradas, README ou CONTRIBUTING), leia [CONTRIBUTING.md](CONTRIBUTING.md), seções **Modelo de entrada** e **Estilo**, e siga as regras e as formulações padrão.

- Confira cada fato na fonte oficial do recurso antes de escrever.
- O índice do README é gerado por `.github/scripts/build_index.py` a partir do frontmatter. Depois de criar, remover ou editar entradas, execute o script em vez de editar o índice à mão. O script também valida as entradas; corrija todos os problemas que ele listar.
- Código (scripts, workflows, comentários) é escrito em inglês, conforme a ADR 0001 do repositório `docs`. Textos, entradas e mensagens de commit ficam em português.
- Uma categoria nova precisa ser registrada em `.portal/config.json`, que define a ordem e os nomes das categorias no índice.
- Ao remover uma entrada, registre o item e o motivo em `docs/fontes/README.md`, no repositório [viveiro-digital/docs](https://github.com/viveiro-digital/docs).
- Para mudanças de estrutura (categorias, seções da entrada, arquivos novos na raiz), pergunte antes à mantenedora.
