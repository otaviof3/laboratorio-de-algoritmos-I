def soma(numero1,numero2):
    somar = numero1 + numero2
    return somar
def parametros():
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    return numero1, numero2
def main():
    numero1, numero2 = parametros()
    somar = soma(numero1,numero2)
    print ("A soma dos números é",somar)
main()
