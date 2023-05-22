def inserir(itens):
    item = input("Insira um item: ")
    itens.append(item)
    return itens
def retirar(itens):
    i = input("Digite um item para ser retirado: ")
    itens.remove(i)
    return itens
def listar(itens):
    print(itens)
def menu():
    print("1 - Inserir item.")
    print("2 - Retirar item.")
    print("3 - Listar itens.")
    print("4 - Sair.")
    opcao = int(input("Digite a opção: "))
    return opcao
def main():
    itens = []
    opcao = 0
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            itens = inserir(itens)
        elif opcao == 2:
            itens = retirar(itens)
        elif opcao == 3:
            listar(itens)
main()