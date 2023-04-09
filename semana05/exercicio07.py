numero = 0
receber = 0
entre3090 = 0
while receber < 10:
    numero = float(input("Digite um número: "))
    if numero >= 30 and numero <= 90:
        entre3090 = entre3090 + 1
    receber = receber + 1
print("A quantidade dos números entre 30 e 90 é",entre3090)