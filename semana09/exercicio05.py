def menu():
    print ("1 - Sacar dinheiro")
    print ("2 - Depositar dinheiro")
    print ("3 - Mostrar saldo")
    print ("4 - Sair")
    opcao = int(input("Opção: "))
    return opcao
def sacar(saldo):
    saque = float(input("Quanto deseja sacar: "))
    if saque <= saldo:
        saldo = saldo - saque
    else:
        print("Saldo insuficiente!")
    return saldo
def depositar(saldo):
    deposito = float(input("Digite o valor do depósito: "))
    saldo = saldo + deposito
    return saldo
def mostrar(saldo):
    print ("Saldo:",saldo)
def main():
    saldo = 0
    opcao = 0
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            saldo = sacar(saldo)
        elif opcao == 2:
            saldo = depositar(saldo)
        elif opcao == 3:
            mostrar(saldo)
main()        