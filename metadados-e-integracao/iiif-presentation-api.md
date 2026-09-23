---
title: "IIIF Presentation API 3.0"
description: "Especificação para apresentação de objetos compostos, como publicações de várias páginas."
type: padrão
tags: [metadados-e-integracao]
created: 2026-09-23
---

[Fonte oficial](https://iiif.io/api/presentation/3.0/)

Especificação do International Image Interoperability Framework (IIIF) para apresentar objetos digitais compostos, como livros e publicações de várias páginas. A versão 3.0 é publicada pelo IIIF Consortium.

## Estrutura

- **Collection**: lista ordenada de manifestos e de outras coleções.
- **Manifest**: um objeto, com seus metadados e suas vistas.
- **Canvas**: cada vista, como uma página.
- **Range**: agrupamento de vistas, como um sumário.

Os documentos são escritos em JSON-LD. Visualizadores compatíveis, como Mirador e Universal Viewer, exibem as páginas em sequência, com zoom e metadados.

## Observações

- **Custo:** acesso gratuito.
- **Instalação:** a exibição com zoom geralmente requer um servidor de imagens compatível com a IIIF Image API.
- **Licença:** CC BY 4.0.
