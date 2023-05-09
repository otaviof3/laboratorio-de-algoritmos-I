def receberNotas():
    notaTotal = 0
    receber = 0
    while receber < 5:
        nota = float(input("Digite uma nota: "))
        notaTotal = notaTotal + nota
        media = notaTotal / 5
        receber = receber + 1
    return media
def aprovado():
    print ("Você está aprovado!")
def recuperacao():
    print ("Você está em recuperação!")
def reprovado():
    print ("Você está reprovado!")
def main():
    media = receberNotas()
    if media >= 7:
         aprovado()
    elif media >= 4 and media < 7:
        recuperacao()
    elif media < 4:
        reprovado()
main()