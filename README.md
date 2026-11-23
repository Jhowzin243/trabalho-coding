# Controle Financeiro Pessoal

Aplicação de linha de comando (CLI) desenvolvida em **Python** para registrar e acompanhar receitas e despesas pessoais de forma simples e interativa.

## Funcionalidades

- **Registrar transação:** permite cadastrar entradas (`receita`) ou saídas (`despesa`) informando uma descrição e um valor numérico válido.
- **Listar transações:** exibe todas as movimentações cadastradas em ordem, indicando o tipo, a descrição e o valor formatado (`+` para receitas e `-` para despesas).
- **Ver resumo do saldo:** calcula automaticamente o total de receitas, o total de despesas e o saldo final, informando se o status está positivo, negativo ou zerado.
- **Validação de entradas:** trata erros de digitação, valores negativos ou zero, descrições vazias e aceita tanto vírgula quanto ponto nos valores decimais.

## Estrutura do Código

O arquivo `trabalho.py` é organizado nas seguintes funções:

- `exibir_menu()`: apresenta as opções principais no terminal.
- `registrar_transacao()`: cria um dicionário com os dados da transação e o adiciona à lista em memória.
- `listar_transacoes()`: percorre e formata todas as transações registradas.
- `calcular_saldo()`: soma as entradas e saídas para retornar os totais e o saldo atual.
- `main()`: gerencia o fluxo principal do programa e as interações com o usuário.

## Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `trabalho.py`.
3. No terminal, navegue até a pasta do projeto e execute:

## Exemplo de Uso

```text
=== CONTROLE FINANCEIRO PESSOAL ===
1 - Registrar transação (receita ou despesa)
2 - Listar transações
3 - Ver resumo do saldo
0 - Sair
Escolha uma opção:
```
