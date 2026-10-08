---
title: "restic"
description: "Ferramenta de backup com versões, deduplicação e criptografia."
type: ferramenta
tags: [tratamento-de-arquivos]
created: 2026-09-23
---

[https://restic.net/](https://restic.net/)

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

## Leitura inicial baseada na fonte oficial

Esta não é uma avaliação de uso pelo Viveiro. A fonte oficial apresenta o restic como um programa de backup que funciona em Linux, BSD, macOS e Windows e grava em vários tipos de armazenamento. Os destaques incluem executável único, transferência apenas das partes alteradas, criptografia, verificação e restauração sem servidor próprio.

Parece adequado para criar cópias de segurança versionadas de arquivos e diretórios. A avaliação prática deve priorizar testes de restauração, proteção das senhas e compatibilidade do repositório de backup com a estratégia de armazenamento escolhida.
