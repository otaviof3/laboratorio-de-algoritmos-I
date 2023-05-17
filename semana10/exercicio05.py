def parametro():
    numero = int(input("Digite um número: "))
    return numero
def somas (numero, i):
    soma = numero + i
    return soma
def main():
    numero = parametro()
    for i in range (0,numero + 1):
        soma = somas (numero, i)
        print (soma)
main()