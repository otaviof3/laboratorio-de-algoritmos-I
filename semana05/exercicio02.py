saldo = float(input("Digite seu saldo: "))
opcao = 0
while opcao != 4:
    print("1 - Sacar.")
    print("2 - Depositar.")
    print("3 - Saldo.")
    print("4 - Sair.")
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        saque = float(input("Saque um valor: "))
        if saldo >= saque:
            saldo = saldo - saque
        else:
            print("Inválido!")
    elif opcao == 2:
        deposito = float(input("Deposite um valor: "))
        saldo = saldo + deposito
    elif opcao == 3:
        print("Seu saldo é",saldo)
    elif opcao == 4:
        print("Obrigado pela confiança!")
    else:
        print("Não brinque com o sistema, por favor...")