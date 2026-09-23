---
title: "BagIt — RFC 8493"
description: "Formato de empacotamento de arquivos com verificação de integridade."
type: padrão
tags: [metadados-e-integracao]
created: 2026-09-23
---

[Fonte oficial](https://www.rfc-editor.org/rfc/rfc8493)

Especificação de um formato de pacote (*bag*) para guardar e transferir arquivos, publicada em outubro de 2018 como RFC 8493, de caráter informativo. Os autores são da California Digital Library, das Stanford Libraries e da Library of Congress.

## Estrutura

- `bagit.txt`: versão do formato e codificação.
- `data/`: pasta com os arquivos.
- Manifesto: lista com o *checksum* de cada arquivo, como `manifest-sha256.txt`.
- Arquivos opcionais, como `bag-info.txt`, com informações sobre o pacote.

Com o manifesto, é possível verificar se algum arquivo foi alterado ou perdido depois de uma cópia ou transferência. As implementações devem aceitar os algoritmos SHA-256 e SHA-512.

## Observações

- **Custo:** acesso gratuito.

## Veja também

- [bagit-python](https://github.com/LibraryOfCongress/bagit-python), biblioteca e ferramenta de linha de comando para criar e verificar pacotes
- [Archivematica](../tratamento-de-arquivos/archivematica.md)
