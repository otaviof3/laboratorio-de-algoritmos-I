print ("Utilize Homem e Mulher para digitar seu sexo, escritos como estão nesta frase (Primeira letra maiúscula).")
sexo = input("Digite seu sexo: ")
h = float(input("Digite sua altura: "))
if sexo == ("Homem"):
    pesoIdealH = (72.7 * h) - 58
    print ("Seu peso ideal é",pesoIdealH)
if sexo == ("Mulher"):
    pesoIdealM = (62.1 * h) - 44.7
    print ("Seu peso ideal é:",pesoIdealM)