intervalo = 0
for i in range (1,11,1):
    numero = float(input("Digite um número: "))
    if numero in range (11,20):
        intervalo = intervalo + 1
nao = 10 - intervalo
print(intervalo,"números estão no intervalo de 10 a 20.")
print(nao,"números não estão no intervalo.")