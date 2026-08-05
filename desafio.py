menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Saldo
[q] Sair

"""

def deposito(valor):
    global saldo, extrato_texto

    if valor > 0:
        saldo += valor
        extrato_texto += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido. O depósito deve ser maior que zero.")


def saque(valor):
    global saldo, extrato_texto, numero_saques

    if valor <= 0:
        print("Valor inválido. O saque deve ser maior que zero.")
    elif valor > limite:
        print("Valor de saque excede o limite de R$ 500,00.")
    elif numero_saques >= limite_saques:
        print("Limite de saques atingido.")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldo -= valor
        extrato_texto += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")


def mostrar_extrato():
    print("\n=== Extrato ===")
    if extrato_texto:
        print(extrato_texto)
    else:
        print("Não foram realizadas movimentações.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("================\n")

saldo = 0
limite = 500
extrato_texto = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu + "Escolha uma opção: ").strip().lower()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        deposito(valor)

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        saque(valor)

    elif opcao == "e":
        mostrar_extrato()

    elif opcao == "c":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")