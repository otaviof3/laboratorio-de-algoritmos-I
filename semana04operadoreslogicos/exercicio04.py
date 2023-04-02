nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 6.0:
    if media >= 9.0:
        conceito = "A"
    elif media >= 7.5:
        conceito = "B"
    elif media >= 6.0:
        conceito = "C"
    print("Suas notas foram",nota1,"e",nota2,", sua média foi",media,"e seu conceito",conceito,)    
    print ("APROVADO!")
elif media < 6.0:
    if media >= 4.0:
        conceito = "D"
    elif media >= 0:
        conceito = "E"
    print("Suas notas foram",nota1,"e",nota2,", sua média foi",media,"e seu conceito",conceito,)
    print ("REPROVADO.")
