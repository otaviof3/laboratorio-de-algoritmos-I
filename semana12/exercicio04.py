def criar(array1, array2):
    for n in range (0,5):
        numero = int(input("Primeira lista: "))
        array1.append(numero)
    for n in range (0,5):
        numero = int(input("Segunda lista: "))
        array2.append(numero)
    return array1, array2
def somar(array1, array2):
    array3 = []
    for n in range(0,5):
        numero = array1[n] + array2[n]
        array3.append(numero)
    print("A soma dos números correspondentes é",array3)
def main():
    array1 = []
    array2 = []
    array1, array2 = criar(array1, array2)
    somar(array1, array2)
main()