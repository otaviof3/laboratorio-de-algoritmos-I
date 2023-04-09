idade = 0
peso = 0
pessoas = 0
maiorDeI = 0
entreDezTrinta = 0
while pessoas < 7:
    idadeP = int(input("Digite sua idade: "))
    pesoP = float(input("Digite seu peso: "))
    idade = idade + idadeP
    pessoas = pessoas + 1
    if idadeP >= 18:
        maiorDeI = maiorDeI + 1
    if idade >= 10 and idade <= 30:
        entreDezTrinta = entreDezTrinta + 1
mediaI = idade / pessoas
porcentagemDezTrinta = entreDezTrinta / 100
print ("A média das idades é",mediaI)
print ("A quantidade de pessoas maiores de idade é",maiorDeI)
print ("A porcentagem de pessoas entre dez e trinta anos é",porcentagemDezTrinta)