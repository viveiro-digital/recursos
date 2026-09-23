---
title: "Robots Exclusion Protocol — RFC 9309"
description: "Especificação do arquivo que indica a robôs de coleta quais páginas não acessar."
type: padrão
tags: [acesso-direitos-e-acessibilidade]
created: 2026-09-23
---

[Fonte oficial](https://www.rfc-editor.org/rfc/rfc9309)

Especificação do arquivo robots.txt, publicada pela Internet Engineering Task Force (IETF) em setembro de 2022 como RFC 9309. Formaliza o protocolo criado em 1994 por Martijn Koster, usado por sites para indicar a robôs de coleta, como buscadores e coletores de dados para treinamento de inteligência artificial, quais páginas não devem ser acessadas.

## Estrutura

- O arquivo fica na raiz do site, em `/robots.txt`.
- Cada grupo de regras começa com `user-agent`, que identifica o robô, seguido de linhas `allow` e `disallow` com os caminhos.
- Robôs podem guardar o arquivo em cache por até 24 horas.

O cumprimento das regras depende de cada robô. A especificação afirma que as regras não são uma forma de autorização de acesso.

## Observações

- **Custo:** acesso gratuito.
