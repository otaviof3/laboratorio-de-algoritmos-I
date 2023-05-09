def receberValor():
    valor = float(input("Valor: "))
    return valor
def dobroValor(valor):
    dobro = valor * 2
    return dobro
def triploValor(valor):
    triplo = valor * 3
    return triplo
def main():
    valor = receberValor()
    dobro = dobroValor(valor)
    triplo = triploValor (valor)
    print ("Seu dobro é:",dobro)
    print ("Seu triplo é:",triplo)
main()