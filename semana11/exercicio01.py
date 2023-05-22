def lerValores(valores):
    for i in range(0,10):
        valor = float(input("Digite um valor: "))
        valores.append(valor)
    return valores
def maiores(valores,maioresQue100,maiorQue100):
    for valor in valores:
        if valor > 100:
            maioresQue100.append(valor)
            maiorQue100 = maiorQue100 + 1
    return maioresQue100, maiorQue100
def main():
    valores = []
    maioresQue100 = []
    maiorQue100 = 0
    valores = lerValores(valores)
    maioresQue100, maiorQue100 = maiores(valores,maioresQue100,maiorQue100)
    print("Quantidade:",maiorQue100, "Números:",maioresQue100)
main()
