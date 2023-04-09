idade = 0
peso = 0
pessoas = 0
maiorDeI = 0
entre1030 = 0
while pessoas < 7:
    idadeP = int(input("Digite sua idade: "))
    pesoP = float(input("Digite seu peso: "))
    idade = idade + idadeP
    pessoas = pessoas + 1
    if idadeP >= 18:
        maiorDeI = maiorDeI + 1
    if idadeP >= 10 and idadeP <= 30:
        entre1030 = entre1030 + 1
mediaI = idade / pessoas
q1030 = entre1030 / 7
porcentagem1030 = q1030 * 100
print ("A média das idades é",mediaI)
print ("A quantidade de pessoas maiores de idade é",maiorDeI)
print ("A porcentagem de pessoas entre dez e trinta anos é",porcentagem1030)
