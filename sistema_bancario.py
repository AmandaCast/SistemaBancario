def exibir_menu():
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """
    return input(menu)

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")
    else:
        print(" Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! Valor excede o limite por saque.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque:    R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Valor inválido para saque.")

    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n========= EXTRATO =========")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("============================")

def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            mostrar_extrato(saldo, extrato)

        elif opcao == "q":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("⚠️ Operação inválida. Tente novamente.")

if __name__ == "__main__":
    main()
