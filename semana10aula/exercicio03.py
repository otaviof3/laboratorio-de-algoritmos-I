def ler (salarioTotal, maiorIdade, menorIdade, quantidade, i):
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo, Masculino (M) ou Feminino (F): ").upper()
    salario = float(input("Digite seu salário: "))
    salarioTotal = salarioTotal + salario
    if i == 0:
        maiorIdade = idade
        menorIdade = idade
    else:
        if idade > maiorIdade:
            maiorIdade = idade
        elif idade < menorIdade:
            menorIdade = idade
    if sexo == "F" and salario <= 100:
        quantidade = quantidade + 1
    return salarioTotal, maiorIdade, menorIdade, quantidade
def media (salarioTotal):
    print("A média dos salários é:",salarioTotal / 10)
def informe (maiorIdade, menorIdade, quantidade):
    print("A maior idade é",maiorIdade)
    print("A menor idade é",menorIdade)
    print("A quantidade de mulheres com salário até 100 é:",quantidade)
def main():
    salarioTotal = 0
    maiorIdade = 0
    menorIdade = 0
    quantidade = 0
    for i in range (0,10):
        salarioTotal, maiorIdade, menorIdade, quantidade = ler(salarioTotal, maiorIdade, menorIdade, quantidade, i)
    media(salarioTotal)
    informe(maiorIdade, menorIdade, quantidade)
main()
