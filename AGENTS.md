# Instruções para agentes

Antes de criar ou editar qualquer texto deste repositório (entradas, README ou CONTRIBUTING), leia [CONTRIBUTING.md](CONTRIBUTING.md), seções **Modelo de entrada** e **Estilo**, e siga as regras e as formulações padrão.

## Registro de aprendizados

Quando a mantenedora corrigir ou aprovar uma forma de trabalhar, registre a regra no mesmo pull request ou commit da mudança:

- Regras de texto, formato de entrada e tom: em [CONTRIBUTING.md](CONTRIBUTING.md), seção **Estilo** ou **Modelo de entrada**.
- Regras de processo, automação e verificação: neste arquivo.
- Decisões de projeto: como ADR em `adr/`, no repositório [viveiro-digital/docs](https://github.com/viveiro-digital/docs).

Escreva a regra de forma geral, com o motivo quando ele não for óbvio, para que valha em situações parecidas. Cada regra fica em um único lugar; nos demais, use um link.

## Verificação de fatos

- Escreva só o que a fonte oficial do recurso confirma. Na dúvida, deixe o fato de fora.
- Se o site bloquear o acesso automatizado, tente o repositório oficial do projeto (por exemplo, no GitHub) ou o documento em PDF. Se nada funcionar, mantenha a entrada com os fatos já confirmados.
- Registre em `docs/fontes/README.md` as fontes que não puderam ser lidas, os links trocados e as informações que vieram de fontes secundárias.
- Ao revisar muitas entradas, mostre antes duas ou três de tipos diferentes à mantenedora e aplique o formato ao restante só depois da aprovação.

## Índice e validação

- O índice do README é gerado por `.github/scripts/build_index.py` a partir do frontmatter. Depois de criar, remover ou editar entradas, execute o script em vez de editar o índice à mão. O script também valida as entradas; corrija todos os problemas que ele listar.
- Uma categoria nova precisa ser registrada em `.portal/config.json`, que define a ordem e os nomes das categorias no índice.
- Ao remover uma entrada, registre o item e o motivo em `docs/fontes/README.md`.

## Automação

- Código (scripts, workflows, comentários) é escrito em inglês, conforme a ADR 0001 do repositório `docs`. Mensagens exibidas a quem contribui (erros de validação, relatórios, comentários em pull requests), textos, entradas e mensagens de commit ficam em português.
- Para testar uma mudança nas GitHub Actions, abra um pull request de teste, confira o resultado e feche sem merge, apagando o branch.
- O workflow `index-comment.yml` roda por `workflow_run`, que sempre usa a versão do arquivo em `main`. Mudanças nele só valem depois do merge.
- `actions/upload-artifact` não aceita caminhos com `..`. Use `$RUNNER_TEMP` para arquivos temporários fora do checkout.
- Prefira automatizar passos repetitivos (como o índice) a pedir que contribuidores os façam à mão.

## Mudanças de estrutura

Para mudanças de estrutura (categorias, seções da entrada, campos do frontmatter, arquivos novos na raiz), pergunte antes à mantenedora.
