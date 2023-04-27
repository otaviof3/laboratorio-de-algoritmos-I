quantidade = 0
azuis = 0
verdes = 0
castanhos = 0
loiro = 0
castanho = 0
preto = 0
masculino = 0
feminino = 0
sexo = input("Digite o seu sexo: ").upper()
corOlhos = input("Digite a cor dos seus olhos: ").upper()
corCabelo = input("Digite a cor do seu cabelo: ").upper()
idade = int(input("Digite sua idade: "))
if sexo == "F" and idade > 18 and idade < 35 and corOlhos == "V" and corCabelo == "L":
    quantidade = quantidade + 1
if corOlhos == "A":
    azuis = azuis + 1
elif corOlhos == "V":
    verdes = verdes + 1
elif corOlhos == "C":
    castanhos = castanhos + 1
if corCabelo == "L":
    loiro = loiro + 1
elif corCabelo == "C":
    castanho = castanho + 1
elif corCabelo == "P":
    preto = preto + 1
if sexo == "M":
    masculino = masculino + 1
elif sexo == "F":
    feminino = feminino + 1
idadeMaior = idade
idadeMenor = idade

for i in range (1,15,1):
    sexo = input("Digite o seu sexo: ").upper()
    corOlhos = input("Digite a cor dos seus olhos: ").upper()
    corCabelo = input("Digite a cor do seu cabelo: ").upper()
    idade = int(input("Digite sua idade: "))
    if idade > idadeMaior:
        idadeMaior = idade
    elif idade < idadeMenor:
        idadeMenor = idade
    if sexo == "F" and idade > 18 and idade < 35 and corOlhos == "V" and corCabelo == "L":
        quantidade = quantidade + 1
    if corOlhos == "A":
        azuis = azuis + 1
    elif corOlhos == "V":
        verdes = verdes + 1
    elif corOlhos == "C":
        castanhos = castanhos + 1
    if corCabelo == "L":
        loiro = loiro + 1
    elif corCabelo == "C":
        castanho = castanho + 1
    elif corCabelo == "P":
        preto = preto + 1
    if sexo == "M":
        masculino = masculino + 1
    elif sexo == "F":
        feminino = feminino + 1
p100A = (azuis / 15) * 100
p100V = (verdes / 15) * 100
p100C = (castanhos / 15) * 100
p100L = (loiro / 15) * 100
p100CC = (castanho / 15) * 100
p100P = (preto / 15) * 100
p100M = (masculino / 15) * 100
p100F = (feminino / 15) * 100
print ("A idade maior é: ",idadeMaior)
print ("A idade menor é: ",idadeMenor)
print ("A quantidade de mulheres entre os 18 e 35 anos com olhos verdes e cabelos louros é:",quantidade)
print ("A porcentagem de pessoas com olhos azuis é: ",p100A)
print ("A porcentagem de pessoas com olhos verdes é: ",p100V)
print ("A porcentagem de pessoas com olhos castanhos é: ",p100C)
print ("A porcentagem de pessoas com cabelos louros é: ",p100L)
print ("A porcentagem de pessoas com cabelos castanhos é: ",p100CC)
print ("A porcentagem de pessoas com cabelos pretos é: ",p100P)
print ("A porcentagem do sexo masculino é: ",p100M)
print ("A porcentagem do sexo feminino é: ",p100F)
