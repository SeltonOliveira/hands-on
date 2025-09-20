print("\n================ Banco HandsOn ================")
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
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu).lower()

    if opcao == "d":
        print("================ DEPÓSITOS ================\n")
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é invalido.")
        
        print("Seu depósito foi realizado com sucesso.\n")
        input("Pressione enter para voltar ao menu de navegação.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.\n")
            input("Pressione enter para voltar ao menu de navegação.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.\n")
            input("Pressione enter para voltar ao menu de navegação.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.\n")
            input("Pressione enter para voltar ao menu de navegação.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Seu saque foi realizado com sucesso!\n")
            input("Pressione enter para voltar ao menu de navegação.")

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "e":
        print("============== EXTRATO ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")
        input("Precione enter para voltar ao menu de navegação.")

    
    elif opcao == "q":
        print("\nBanco HandsOn agradece sua preferencia.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")