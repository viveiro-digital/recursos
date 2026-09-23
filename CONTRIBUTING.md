---
title: Como contribuir
description: Como sugerir, corrigir ou acrescentar um recurso.
---

# Como contribuir

Obrigado pelo interesse! Este repositório é só Markdown: não é preciso instalar nada.

## Sugerir um recurso sem editar arquivos

Abra uma [issue](https://github.com/viveiro-digital/recursos/issues/new) com:

- nome do recurso e link, de preferência para a fonte oficial;
- uma ou duas frases sobre o problema que ele ajuda a resolver e para quem;
- a categoria que parece mais adequada;
- se você já usou o recurso, conte em que contexto e quais foram suas impressões.

## Acrescentar ou corrigir um recurso por pull request

Cada recurso fica em um arquivo próprio, dentro da pasta da sua categoria.

1. Escolha a pasta da categoria. Se nenhuma servir, explique no pull request; não crie pastas vazias.
2. Crie um arquivo com o nome do recurso em minúsculas, sem acentos e com hífens, por exemplo `preservacao-digital/ndsa-levels-of-digital-preservation.md`.
3. Use o modelo abaixo.
4. Acrescente uma linha para o recurso no `README.md` da categoria.
5. Abra o pull request.

Antes de criar um arquivo, procure o link no repositório: se o recurso já existir, melhore a entrada existente.

### Modelo

```markdown
---
title: Nome do recurso
description: Uma frase sobre o que é o recurso.
type: guia
tags: [nome-da-categoria]
created: AAAA-MM-DD
---

[Fonte oficial](https://exemplo.org/)

O problema que o recurso ajuda a resolver e para quem ele se destina.

## Observações

- Requisitos, limites conhecidos ou outras observações.

## Nossa experiência

Opcional: só quando o recurso foi usado. Conte em que contexto, o que funcionou, o que não funcionou e dicas para quem for usar.
```

- `type`: `ferramenta`, `guia`, `padrão`, `artigo`, `iniciativa`, `comunidade` ou `acervo`.
- A primeira linha depois do cabeçalho é sempre o link para a fonte oficial.
- Use links relativos para outros arquivos do repositório, como `[texto](../outra-categoria/arquivo.md)`.

## Cuidados

- Descreva o recurso pelo que ele oferece. Impressões de uso vão na seção "Nossa experiência", separadas do que o fornecedor ou a organização diz.
- Citações de outros textos devem ser curtas e indicar a autoria.
- Para propor um guia ou relato de experiência, abra uma issue primeiro. Respeite a autoria e as condições de uso dos materiais citados, e não inclua dados pessoais de terceiros.

## Licença das contribuições

Ao contribuir, você concorda em publicar seu texto sob a mesma licença do repositório, [CC BY 4.0](LICENSE).

## Contato

bibliotecadezines@gmail.com
