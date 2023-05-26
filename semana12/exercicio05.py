import random
def criar(array):
    for n in range (0,10):
        numero = random.randint(1,100)
        array.append(numero)
    return array
def pares(array):
    for n in range (0,10):
        if array[n] % 2 == 0:
            print(array[n])
def main():
    array = []
    array = criar(array)
    pares(array)
main()