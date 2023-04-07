idadeX = 0
alturaX = 0
opcao = 0
pessoas = 0
while opcao != 3:
    print("1 - Cadastrar pessoa.")
    print("2 - Mostrar média de idade e altura.")
    print("3 - Sair.")
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        idade = int(input("Digite sua idade: "))
        altura = float(input("Digite sua altura: "))
        idadeX = idadeX + idade
        alturaX = alturaX + altura
        pessoas = pessoas + 1
    elif opcao == 2:
        mediaIdade = idadeX / pessoas
        mediaAltura = alturaX / pessoas
        print("A média de idade é:",mediaIdade)
        print("A média de altura é:",mediaAltura)
    elif opcao == 3:
        mediaIdade = idadeX / pessoas
        mediaAltura = alturaX / pessoas
        print("Usuário saiu.")
        print("A média de idade é:",mediaIdade)
        print("A média de altura é:",mediaAltura)
    else:
        print("Opção inválida!")
