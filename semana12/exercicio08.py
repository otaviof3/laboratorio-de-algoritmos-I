def menu():
    print("1 - Inserir item")
    print("2 - Listar itens")
    print("3 - Retirar item")
    print("4 - Retirar todos os itens")
    print("5 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao
def inserir(array):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        array.append(numero)
        return array
    else:
        print("Erro! Digite um número par!")
        return array
def listar(array):
    print(array)
def retirar(array):
    numero = int(input("Digite um número para retirar: "))
    array.remove(numero)
    return array
def retirarTodos(array):
    array = []
    return array
def algoritmo(opcao, array):
    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            array = inserir(array)
        elif opcao == 2:
            listar(array)
        elif opcao == 3:
            array = retirar(array)
        elif opcao == 4:
            array = retirarTodos(array)
def main():
    array = []
    opcao = 0
    algoritmo(opcao, array)
main()