def vezes2(numero):
    dobro = numero * 2
    return dobro
def parametros():
    numero = float(input("Digite um número: "))
    return numero
def main():
    numero = parametros()
    dobro = vezes2(numero)
    print ("O dobro do número é",dobro)
main()