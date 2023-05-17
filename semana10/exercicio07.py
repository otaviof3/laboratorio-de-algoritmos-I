def jornal ():
    entrevista = input("Qual jornal você prefere (A, B ou C): ").upper()
    return entrevista
def resposta (entrevista, a, b, c):
    if entrevista == "A":
        a = a + 1
    elif entrevista == "B":
        b = b + 1
    elif entrevista == "C":
        c = c + 1
    return a, b, c
def porcentagem(a, b, c):
    porcentA = (a * 100) / 20
    porcentB = (b * 100) / 20
    porcentC = (c * 100) / 20
    return porcentA, porcentB, porcentC
def final (porcentA, porcentB, porcentC):
    if porcentA < porcentB and porcentA < porcentC:
        print("A porcentagem de pessoas que preferem o jornal A é",porcentA)
        if porcentB < porcentC:
            print("A porcentagem de pessoas que preferem o jornal B é",porcentB)
            print("A porcentgaem de pessoas que preferem o jornal C é",porcentC)
        else:
            print("A porcentgaem de pessoas que preferem o jornal C é",porcentC)
            print("A porcentagem de pessoas que preferem o jornal B é",porcentB)
    elif porcentB < porcentC:
        print("A porcentagem de pessoas que preferem o jornal B é",porcentB)
        if porcentA < porcentC:
            print("A porcentagem de pessoas que preferem o jornal A é",porcentA)
            print("A porcentgaem de pessoas que preferem o jornal C é",porcentC)
        else:
            print("A porcentgaem de pessoas que preferem o jornal C é",porcentC)
            print("A porcentagem de pessoas que preferem o jornal A é",porcentA)
    else:
        print("A porcentgaem de pessoas que preferem o jornal C é",porcentC)
        if porcentA < porcentB:
            print("A porcentagem de pessoas que preferem o jornal A é",porcentA)
            print("A porcentagem de pessoas que preferem o jornal B é",porcentB)
        else:
            print("A porcentagem de pessoas que preferem o jornal B é",porcentB)
            print("A porcentagem de pessoas que preferem o jornal A é",porcentA)
def main():
    a = 0
    b = 0
    c = 0
    for i in range (0,20):
        entrevista = jornal()
        a, b, c = resposta(entrevista, a, b, c)
    porcentA, porcentB, porcentC = porcentagem(a, b, c)
    final(porcentA, porcentB, porcentC)
main()