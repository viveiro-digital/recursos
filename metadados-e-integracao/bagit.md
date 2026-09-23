---
title: "BagIt — RFC 8493"
description: "Formato de empacotamento de arquivos com verificação de integridade (RFC 8493)."
type: padrão
tags: [metadados-e-integracao]
created: 2026-09-23
---

[Fonte oficial](https://www.rfc-editor.org/rfc/rfc8493)

Especificação de um formato de pacote (*bag*): uma pasta com os arquivos e um manifesto com o *checksum* de cada um. O manifesto permite verificar se algum arquivo foi alterado ou perdido depois de uma cópia ou transferência.

O formato é usado por ferramentas de preservação, como o Archivematica.

## Veja também

- [bagit-python](https://github.com/LibraryOfCongress/bagit-python), biblioteca e ferramenta de linha de comando para criar e verificar pacotes
- [Archivematica](../tratamento-de-arquivos/archivematica.md)
