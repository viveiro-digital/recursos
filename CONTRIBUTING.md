---
title: Como contribuir
description: Como sugerir, corrigir ou acrescentar um recurso.
---

# Como contribuir

Este repositório contém apenas arquivos Markdown. Não é preciso instalar nada para contribuir.

## Sugerir um recurso por issue

Abra uma [issue](https://github.com/viveiro-digital/recursos/issues/new) com as seguintes informações:

- Nome do recurso e link para a fonte oficial.
- Uma ou duas frases sobre o que o recurso faz.
- A categoria mais adequada.
- Contexto de uso, se você já usou o recurso.

## Acrescentar ou corrigir um recurso por pull request

Cada recurso tem um arquivo próprio, na pasta da sua categoria. As categorias estão listadas no [README](README.md#categorias).

1. Procure o link do recurso no repositório. Se o recurso já existir, edite a entrada existente.
2. Escolha a pasta da categoria. Se nenhuma for adequada, explique no pull request. Não crie pastas vazias.
3. Crie um arquivo com o nome do recurso em minúsculas, sem acentos e com hífens. Por exemplo: `preservacao-digital/ndsa-levels-of-digital-preservation.md`.
4. Preencha o arquivo conforme o modelo da próxima seção.
5. Abra o pull request.

## Modelo de entrada

```markdown
---
title: Nome do recurso
description: Uma frase sobre o que o recurso é.
type: ferramenta
tags: [nome-da-categoria]
created: AAAA-MM-DD
---

[Fonte oficial](https://exemplo.org/)

O que o recurso é, quem o mantém e o que ele faz.

## Observações

- Público a que se destina, se for restrito (por exemplo, instituições com equipe técnica).
- Requisitos de uso (por exemplo, servidor próprio ou uso do terminal).
- Idioma, se não for inglês.
- Formato, se for PDF ou download.

## Veja também

- [Link relacionado](https://exemplo.org/outra-pagina)

## Uso no Viveiro

Contexto em que o recurso foi usado, resultados e limitações encontradas.
```

As seções **Observações**, **Veja também** e **Uso no Viveiro** são opcionais. **Uso no Viveiro** só se aplica a recursos que o Viveiro usou.

Valores aceitos em `type`: `ferramenta`, `guia`, `padrão`, `política`, `publicação`, `legislação`, `iniciativa`, `comunidade` e `acervo`.

## Estilo

Todo texto do repositório (entradas, README e este arquivo) segue os guias de estilo do [Astro](https://contribute.docs.astro.build/guides/writing-style/) e do [MDN](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide). O tom é profissional, neutro e objetivo.

### Regras

- **Fatos verificáveis.** Descreva o que o recurso é, quem o mantém e o que faz, com base na fonte oficial. Opiniões e impressões de uso ficam na seção **Uso no Viveiro**.
- **Descrição, não recomendação.** O texto informa; a decisão de usar é de quem lê. Frases sobre por que o recurso importa ou o que o leitor deveria fazer ficam fora das entradas.
- **Adjetivos descritivos.** Use adjetivos que descrevem (livre, gratuito, institucional) e deixe de fora os que avaliam (ótimo, essencial, um dos melhores).
- **Terceira pessoa e voz impessoal.** Escreva "O Viveiro usou", "Requer servidor próprio", e não "nós usamos" ou "você vai precisar".
- **Frases curtas**, com uma ideia por frase, no presente.
- **Siglas por extenso** na primeira ocorrência: "Instituto Brasileiro de Informação em Ciência e Tecnologia (IBICT)".
- **Termos em outro idioma** em itálico, com tradução quando útil: "*checksum*", "*Findable* (localizáveis)".
- **Referências por nome**, sem indicações de posição como "abaixo" ou "acima": "conforme o modelo da próxima seção".
- **Link para a fonte oficial** sempre na primeira linha depois do cabeçalho.
- **Links relativos** para outros arquivos do repositório, como `[texto](../outra-categoria/arquivo.md)`.
- **Citações curtas**, com autoria.
- **Somente dados públicos.** Não inclua dados pessoais de terceiros.

### Formulações padrão

Use as mesmas formulações em todas as entradas, para que sejam comparáveis:

| Informação | Formulação |
| --- | --- |
| Público restrito | "Voltado a instituições com equipe técnica." |
| Requisitos | "Requer servidor próprio." / "Requer uso do terminal." / "Requer Java." |
| Licença e custo | "Gratuito e de código aberto." / "Norma paga." |
| Idioma | "Em português." (só quando não for inglês) |
| Formato | "Arquivo PDF." / "Arquivo para download." |
| Aspecto jurídico | "Não substitui orientação jurídica." |

### Exemplo de entrada

```markdown
---
title: "restic"
description: "Ferramenta de backup com versões, deduplicação e criptografia."
type: ferramenta
tags: [tratamento-de-arquivos]
created: 2026-09-23
---

[Fonte oficial](https://restic.net/)

Ferramenta de backup que copia pastas para um disco externo ou para um serviço de armazenamento em nuvem. Mantém versões anteriores dos arquivos (*snapshots*), armazena cada conteúdo uma única vez (deduplicação) e criptografa os dados.

## Observações

- Gratuita e de código aberto.
- Requer uso do terminal.
```

Para propor um guia ou relato de experiência, abra uma issue antes.

## Licença das contribuições

As contribuições são publicadas sob a mesma licença do repositório, [CC BY 4.0](LICENSE).

## Contato

[bibliotecadezines@gmail.com](mailto:bibliotecadezines@gmail.com)
