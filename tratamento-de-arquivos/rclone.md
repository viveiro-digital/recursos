---
title: "rclone"
description: "Ferramenta para copiar e sincronizar arquivos entre armazenamento local e em nuvem."
type: ferramenta
tags: [tratamento-de-arquivos]
created: 2026-09-23
---

[https://rclone.org/](https://rclone.org/)

Ferramenta de linha de comando para gerenciar arquivos em serviços de armazenamento em nuvem.

## Funcionalidades

- Mais de 70 serviços suportados, como Google Drive, Dropbox, OneDrive e Amazon S3, além de SFTP e WebDAV.
- Cópia, sincronização em um ou nos dois sentidos, movimentação e verificação por *checksum* (MD5 e SHA-1).
- Criptografia de arquivos com o recurso `crypt`.
- Montagem de um armazenamento em nuvem como disco local.

## Observações

- **Custo:** gratuito.
- **Instalação:** programa para computador (Windows, macOS, Linux e FreeBSD).
- **Conhecimento técnico:** uso do terminal. Há uma interface web experimental.
- **Licença:** MIT.

## Leitura inicial baseada na fonte oficial

Esta não é uma avaliação de uso pelo Viveiro. A fonte oficial apresenta o rclone como um programa de linha de comando para gerenciar arquivos em mais de 70 serviços de armazenamento, sistemas locais e protocolos, com cópia, sincronização, montagem, verificação por hashes, criptografia e retomada de transferências.

Parece adequado para rotinas de cópia, migração e verificação de arquivos em diferentes armazenamentos. A avaliação prática deve começar com `--dry-run`, políticas de retenção e testes de restauração antes de operações destrutivas.
