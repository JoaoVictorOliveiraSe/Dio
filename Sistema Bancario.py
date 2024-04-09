# SISTEMA BANCARIO EM PYTHON

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do déposito: "))
        print("Déposito efetuado com sucesso!")

        if valor > 0:
            saldo += valor
            extrato += "Depósito: R$ {:.2f}\n".format(valor)

        else:
            print ("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))
        print ("Saque efetuado com sucesso!")

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print ("Operação falhou! Você excedeu o limite")

        elif valor > 0:
            saldo -= valor
            extrato += "Saque: R$ {:.2f}\n".format(valor)
            numero_saque += 1

        else:
            print ("Operação falhou! Número máximo de saques excedido")

    elif opcao == "e":
        print("\n ========= EXTRATO ==========")
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print ("\nSaldo: R$ {:.2f}".format(saldo))
        print ("=============================")

    elif opcao == "q":
        print ("Obrigado por utilizar nosso Canal Bancario!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
