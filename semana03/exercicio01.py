horas = float(input("Digite quantas horas trabalhadas no mês: "))
salario = 35.00 * horas
if salario < 1000.00:
    salarioD = salario + 300.00
    print ("Seu salário é:",salarioD)
else:
    print ("Seu salario é:",salario)
