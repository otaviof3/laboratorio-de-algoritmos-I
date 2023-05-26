def solicitar(array):
    for n in range (0,5):
        numero = int(input("Digite um número: "))
        array.append(numero)
    return array
def encontrar(array):
    maior = array[0]
    menor = array[0]
    maiorP = 0
    menorP = 0
    for n in range(0,5):
        if maior < array[n]:
            maior = array[n]
            maiorP = n
        if menor > array[n]:
            menor = array[n]
            menorP = n
    print("O maior número é",maior,"e sua posição",maiorP)
    print("O menor número é",menor,"e sua posição",menorP)
def main():
    array = []
    array = solicitar(array)
    encontrar(array)
main()