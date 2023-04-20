zero = 0
par = 0
impar = 0
for i in range (1,11,1):
    numero = int(input("Digite um número: "))
    if numero == 0:
        zero = zero + 1
    elif numero% 2 == 0:
        par = par + 1
    elif numero% 2 != 0:
        impar = impar + 1
print ("A quantidade de números pares é:",par)
print ("A quantidade de números ímpares é:",impar)
print ("A quantidade de zeros digitados é",zero)