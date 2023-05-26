import random
def criar(array):
    for n in range (0,10):
        numero = random.randint(1,50)
        array.append(numero)
    return array
def parImpar(array):
    par = 0
    impar = 0
    for n in range (0,10):
        if array[n] % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
    print(array)
    print("A quantidade de pares é",par)
    print("A quantidade de ímpares é",impar)
def main():
    array =[]
    array = criar(array)
    parImpar(array)
main()