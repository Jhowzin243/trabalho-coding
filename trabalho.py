def exibir_menu():
    """mostra as opções principais do sistema"""
    print("\n=== CONTROLE FINANCEIRO PESSOAL ===")
    print("1 - Registrar transação (receita ou despesa)")
    print("2 - Listar transações")
    print("3 - Ver resumo do saldo")
    print("0 - Sair")
 
 
def registrar_transacao(transacoes, tipo, descricao, valor):
    """Adiciona uma nova transação à lista"""
    transacao = {
        "tipo": tipo,
        "descricao": descricao,
        "valor": valor
    }
    transacoes.append(transacao)
    return transacao
 
 
def listar_transacoes(transacoes):
    """Exibe todas as transações cadastradas."""
    print("\n--- LISTA DE TRANSAÇÕES ---")
    if not transacoes:
        print("Nenhuma transação registrada até o momento.")
        return
 
    for i, item in enumerate(transacoes, start=1):
        sinal = "+" if item["tipo"] == "receita" else "-"
        print(f"{i}. [{item['tipo'].upper()}] {item['descricao']}: {sinal}R$ {item['valor']:.2f}")
 
 
def calcular_saldo(transacoes):
    """Calcula e  as retorna receitas, despesas e saldo final."""
    total_receitas = 0.0
    total_despesas = 0.0
 
    for item in transacoes:
        if item["tipo"] == "receita":
            total_receitas += item["valor"]
        elif item["tipo"] == "despesa":
            total_despesas += item["valor"]
 
    saldo = total_receitas - total_despesas
    return total_receitas, total_despesas, saldo
 
 
def main():
    transacoes = []
 
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
 
        if opcao == "1":
            tipo_escolha = input("Tipo (1 - ENTRADA | 2 - SAIDA): ").strip()
 
            if tipo_escolha == "1":
                tipo = "receita"
            elif tipo_escolha == "2":
                tipo = "despesa"
            else:
                print("Tipo inválido. Use 1 para receita ou 2 para despesa.")
                continue
 
            descricao = input("Descrição: ").strip()
            if not descricao:
                print("A descrição não pode ficar vazia.")
                continue
 
            try:
                valor = float(input("Valor (ex.: 150.00): ").replace(",", "."))
                if valor <= 0:
                    print("O valor deve ser maior que zero.")
                    continue
            except ValueError:
                print("Valor inválido. Digite apenas números.")
                continue
 
            registrada = registrar_transacao(transacoes, tipo, descricao, valor)
            print(f"Transação registrada: {registrada['descricao']} (R$ {registrada['valor']:.2f}).")
 
        elif opcao == "2":
            listar_transacoes(transacoes)
 
        elif opcao == "3":
            receitas, despesas, saldo = calcular_saldo(transacoes)
            print("\n--- RESUMO FINANCEIRO ---")
            print(f"Total de receitas: R$ {receitas:.2f}")
            print(f"Total de despesas: R$ {despesas:.2f}")
            print(f"Saldo atual:       R$ {saldo:.2f}")
 
            if saldo > 0:
                print("Status: Saldo positivo.")
            elif saldo < 0:
                print("Status: Atenção, saldo negativo!")
            else:
                print("Status: Saldo zerado.")
 
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
 
        else:
            print("Opção inválida. Tente novamente.")
 
 
if __name__ == "__main__":
    main()