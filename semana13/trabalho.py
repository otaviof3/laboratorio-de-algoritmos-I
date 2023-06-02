def menu():
    print("1. Verificar o total de horas trabalhadas e ausentes de um funcionário.")
    print("2. Alterar o total de horas trabalhadas de um funcionário.")
    print("3. Alterar o total de horas ausentes de um funcionário.")
    print("4. Mostrar o salário de um funcionário.")
    print("5. Apresentar as informações de todos os funcionários.")
    print("6. Resetar o vetor.")
    print("7. Sair.")
    opc = int(input("Opção: "))
    return opc
def verificar(horasT, horasA):
    funcionario = int(input("Código (1 a 20): "))
    if funcionario > 0 and funcionario <= 20:
        print("Horas Trabalhadas:",horasT[funcionario - 1])
        print("Horas Ausentes:",horasA[funcionario - 1])
    else:
        print("Inválido.")
def alterarT(horasT, horasA):
    funcionario = int(input("Código (1 a 20): "))
    trabalhadas = int(input("Horas trabalhadas: "))
    if trabalhadas >= 0  and trabalhadas <= 44 and funcionario > 0 and funcionario <= 20:
        horasT[funcionario - 1] = trabalhadas
        horasA[funcionario - 1] = 44 - trabalhadas
    else:
        print("Inválido.")
    return horasT, horasA
def alterarA(horasT, horasA):
    funcionario = int(input("Código (1 a 20): "))
    ausentes = int(input("Horas ausentes: "))
    if ausentes >= 0 and ausentes <= 44 and funcionario > 0 and funcionario <= 20:
        horasA[funcionario - 1] = ausentes
        horasT[funcionario - 1] = 44 - ausentes
    else:
        print("Inválido.")
    return horasT, horasA
def salario(horasT):
    funcionario = int(input("Código (1 a 20): "))
    if funcionario > 0 and funcionario <= 20:
        print("Salário do funcionário:",horasT[funcionario - 1] * 50)
    else:
        print("Inválido.")
def informacoes(horasT,horasA):
    for i in range (0,20):
        print("Código",i + 1,"- Horas Trabalhadas:",horasT[i],"- Horas Ausentes:",horasA[i])
def empresa(horasT,horasA):
    opc = 0
    while opc != 7:
        opc = menu()
        if opc == 1:
            verificar(horasT, horasA)
        elif opc == 2:
            horasT, horasA = alterarT(horasT,horasA)
        elif opc == 3:
            horasT, horasA = alterarA(horasT,horasA)
        elif opc == 4:
            salario(horasT)
        elif opc == 5:
            informacoes(horasT,horasA)
        elif opc == 6:
            horasT, horasA = listas()
def listas():
    horasT =[]
    horasA = []
    for i in range (0,20):
        horasT.append(0)
        horasA.append(44)
    return horasT, horasA
def main():
    horasT, horasA = listas()
    empresa(horasT,horasA)
main()