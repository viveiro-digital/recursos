---
title: "OAI-PMH"
description: "Protocolo para coleta de metadados entre repositórios."
type: padrão
tags: [metadados-e-integracao]
created: 2026-09-23
---

[Fonte oficial](https://www.openarchives.org/OAI/openarchivesprotocol.html)

Protocolo da Open Archives Initiative para coleta de metadados entre sistemas. A versão 2.0 é de junho de 2002. Provedores de dados expõem seus metadados, e provedores de serviço os coletam para criar serviços como catálogos agregados.

## Estrutura

- Seis operações: `Identify`, `ListMetadataFormats`, `ListSets`, `ListIdentifiers`, `ListRecords` e `GetRecord`.
- Requisições HTTP e respostas em XML.
- Dublin Core simples (`oai_dc`) como formato obrigatório.
- Coleta seletiva por data e por conjunto (*set*).

No Brasil, o Oasisbr, do Instituto Brasileiro de Informação em Ciência e Tecnologia (IBICT), usa o protocolo para reunir registros de repositórios do país. DSpace e AtoM oferecem suporte ao protocolo.

## Observações

- **Custo:** acesso gratuito.

## Veja também

- [Oasisbr](https://oasisbr.ibict.br/)
