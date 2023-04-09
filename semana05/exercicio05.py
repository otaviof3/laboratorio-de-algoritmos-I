print("Digite o sexo como M ou F.")
idade = 0
salario = 0
sexo = 0
habitantes = 0
idadeMaior = 0
idadeMenor = 1000
mulher = 0
while habitantes < 10:
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: ").upper()
    salarioH = float(input("Digite seu salário: "))
    salario = salario + salarioH
    if idade >= idadeMaior:
        idadeMaior = idade
    if idade <= idadeMenor:
        idadeMenor = idade
    if sexo == "F" and salarioH <= 100:
        mulher = mulher + 1
    habitantes =  habitantes + 1
media = salario / habitantes
print ("A média de salário é",media)
print ("A maior idade do grupo é",idadeMaior,"e a menor é",idadeMenor)
print ("A quantidade de mulheres com salário até R$100.00 é",mulher)