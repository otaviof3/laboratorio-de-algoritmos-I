def solicitar(array):
    for n in range (0,5):
        numero = int(input("Digite um número: "))
        array.append(numero)
    return array
def somar(array):
    soma = 0
    for n in range (0,5):
        soma = soma + array[n]
    print("A soma é",soma)
    print("A média é",soma / 5)
def main():
    array = []
    array = solicitar(array)
    somar(array)
main()