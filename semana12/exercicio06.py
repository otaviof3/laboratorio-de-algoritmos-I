def solicitar(array):
    for n in range (0,5):
        numero = int(input("Digite um número: "))
        array.append(numero)
    return array
def verificar(array):
    vezes = 0
    numero = int(input("Verifique um número: "))
    for n in array:
        if numero == n:
            vezes = vezes + 1
    print("O número está na lista",vezes,"vez(es)")
def main():
    array = []
    array = solicitar(array)
    verificar(array)
main()