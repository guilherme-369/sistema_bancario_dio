menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Quanto você deseja depositar? "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!!")
        else:
            print("O valor informado é inválido")

    elif opcao == ("s"):
        valor_saque = float(input("Quantia: R$ "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques > LIMITE_SAQUE

        if excedeu_saldo:
            print(f"Operação falhou! Saldo insuficiente. Seu saldo atual é de R$ {saldo:.2f}.")
        
        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f} por operação.")
        
        elif excedeu_saques:
            print(f"Operação falhou! Você já atingiu o limite de {LIMITE_SAQUE} saques diários.")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        
        else:
            print(f"Operação falhou, valor informado inválido.")

    elif opcao == ("e"):
        print("\n================ EXTRATO ================")

        if not extrato:
            print("Sem movimentações")
        else:
            print(extrato)
        
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=========================================")
    
    elif opcao == ("q"):
        break

    else:
        print("Operação inválida, tente novamente")

