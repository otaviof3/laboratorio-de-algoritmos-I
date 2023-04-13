idade = 0
pessoas = 0
maiorIgual18 = 0
while pessoas < 10:
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        maiorIgual18 = maiorIgual18 + 1
    pessoas = pessoas + 1
print("A quantidade de pessoas com idade maior ou igual a 18 é",maiorIgual18)
