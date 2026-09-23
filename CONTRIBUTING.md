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

Cada recurso tem um arquivo próprio, na pasta da sua categoria. As categorias e as entradas estão listadas no [índice do README](README.md#índice).

1. Procure o link do recurso no repositório. Se o recurso já existir, edite a entrada existente.
2. Escolha a pasta da categoria. Se nenhuma for adequada, explique no pull request. Não crie pastas vazias.
3. Crie um arquivo com o nome do recurso em minúsculas, sem acentos e com hífens. Por exemplo: `preservacao-digital/ndsa-levels-of-digital-preservation.md`.
4. Preencha o arquivo conforme o modelo da próxima seção.
5. Abra o pull request.

O índice do README é gerado automaticamente a partir dos campos `title` e `description` de cada entrada. Ao abrir o pull request, uma GitHub Action valida as entradas e atualiza o índice. O resultado aparece em um comentário no pull request, atualizado a cada novo commit, e no resumo da execução da Action. O trecho entre os marcadores `indice:inicio` e `indice:fim` não deve ser editado à mão.

A validação falha, com a lista de problemas, nos seguintes casos:

- Título ou link da fonte oficial igual ao de outra entrada.
- Campo `title`, `description`, `type` ou `tags` ausente.
- `description` igual ao título ou sem ponto final.
- `type` fora dos valores aceitos, ou `tags` sem a pasta da categoria.
- Primeira linha depois do cabeçalho diferente de `[Fonte oficial](...)`.
- Nome de arquivo com maiúsculas, acentos ou espaços.
- Pasta que não está registrada como categoria em `.portal/config.json`.

Para validar e ver o índice localmente, execute `python3 .github/scripts/build_index.py`.

## Modelo de entrada

```markdown
---
title: Nome do recurso
description: Uma frase sobre o que o recurso é, sem repetir o título.
type: ferramenta
tags: [nome-da-categoria]
created: AAAA-MM-DD
---

[Fonte oficial](https://exemplo.org/)

O que o recurso é, quem o mantém e o que ele faz.

## Funcionalidades

- O que o recurso oferece, um item por linha.

## Observações

- **Custo:** gratuito.
- **Instalação:** requer servidor próprio.
- **Conhecimento técnico:** administração de servidores.
- **Licença:** GNU GPL 3.0.

## Veja também

- [Link relacionado](https://exemplo.org/outra-pagina)

## Uso no Viveiro

Contexto em que o recurso foi usado, resultados e limitações encontradas.
```

A seção de conteúdo depende do tipo de recurso:

| Tipo de recurso | Seção |
| --- | --- |
| Ferramentas, sites e acervos | **Funcionalidades** |
| Padrões, especificações e princípios | **Estrutura** |
| Textos, guias, políticas e leis | **Conteúdo** |
| Organizações, redes e projetos | **Atividades** |

As seções de conteúdo, **Observações**, **Veja também** e **Uso no Viveiro** são opcionais. **Uso no Viveiro** só se aplica a recursos que o Viveiro usou.

Valores aceitos em `type`: `ferramenta`, `guia`, `padrão`, `política`, `publicação`, `legislação`, `iniciativa`, `comunidade` e `acervo`.

## Estilo

Todo texto do repositório (entradas, README e este arquivo) segue os guias de estilo do [Astro](https://contribute.docs.astro.build/guides/writing-style/) e do [MDN](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide). O tom é profissional, neutro e objetivo.

### Regras

- **Fatos verificáveis.** Descreva o que o recurso é, quem o mantém e o que faz, com base na fonte oficial. Opiniões e impressões de uso ficam na seção **Uso no Viveiro**.
- **Descrição, não recomendação.** O texto informa; a decisão de usar é de quem lê. Frases sobre por que o recurso importa ou o que o leitor deveria fazer ficam fora das entradas.
- **Adjetivos descritivos.** Use adjetivos que descrevem (livre, gratuito, colaborativo) e deixe de fora os que avaliam (ótimo, essencial, um dos melhores).
- **Terceira pessoa e voz impessoal.** Escreva "O Viveiro usou", "Requer servidor próprio", e não "nós usamos" ou "você vai precisar".
- **Frases curtas**, com uma ideia por frase, no presente.
- **Siglas por extenso** na primeira ocorrência: "Instituto Brasileiro de Informação em Ciência e Tecnologia (IBICT)".
- **Termos em outro idioma** em itálico, com tradução quando útil: "*checksum*", "*Findable* (localizáveis)".
- **Referências por nome**, sem indicações de posição como "abaixo" ou "acima": "conforme o modelo da próxima seção".
- **Link para a fonte oficial** sempre na primeira linha depois do cabeçalho.
- **Links relativos** para outros arquivos do repositório, como `[texto](../outra-categoria/arquivo.md)`.
- **Citações curtas**, com autoria.
- **Somente dados públicos.** Não inclua dados pessoais de terceiros.

### Observações

A seção **Observações** usa itens rotulados, sempre nesta ordem e com estas formulações, para que as entradas sejam comparáveis. Inclua apenas os itens que se aplicam e que a fonte oficial confirma.

| Item | Formulações |
| --- | --- |
| **Custo** | "gratuito." / "acesso gratuito." / "pago." / "gratuito. [Organização] oferece hospedagem e suporte pagos." / "não informado na fonte oficial." |
| **Instalação** | "não requer (serviço online)." / "programa para computador (sistemas)." / "requer servidor próprio." |
| **Conhecimento técnico** | "não requer (interface gráfica)." / "uso do terminal." / "administração de servidores." |
| **Licença** | Nome da licença, como "GNU GPL 3.0." ou "CC BY 4.0." |
| **Idioma** | Só quando não for inglês: "português." |
| **Formato** | Para documentos: "PDF, 25 páginas." |

O público do recurso é descrito por esses fatos práticos. Não classifique recursos pelo porte de quem os usa (como "voltado a grandes instituições"): quem lê decide se o recurso serve ao seu contexto.

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

Programa de backup que copia arquivos para um disco local ou para serviços de armazenamento, próprios ou em nuvem.

## Funcionalidades

- Transfere apenas as partes dos arquivos que mudaram desde o último backup.
- Criptografa os dados em todas as etapas.
- Mantém versões anteriores (*snapshots*), que podem ser restauradas individualmente.
- Verifica se os backups podem ser restaurados.

## Observações

- **Custo:** gratuito.
- **Instalação:** programa para computador (Linux, BSD, macOS e Windows), distribuído como um único executável.
- **Conhecimento técnico:** uso do terminal.
- **Licença:** BSD 2-Clause.
```

Para propor um guia ou relato de experiência, abra uma issue antes.

## Licença das contribuições

As contribuições são publicadas sob a mesma licença do repositório, [CC BY 4.0](LICENSE).

## Contato

[bibliotecadezines@gmail.com](mailto:bibliotecadezines@gmail.com)
