a = 0
b = 0
c = 0
for x in range (1,21,1):
    jornal = input("Jornal A, B ou C? Sua opinião: ").upper()
    if jornal == "A":
        a = a +1
    elif jornal == "B":
        b = b + 1
    elif jornal == "C":
        c = c + 1
porcentA = (a / 20) * 100
porcentB = (b / 20) * 100
porcentC = (c / 20) * 100
if a < b and a < c:
    print("A porcentagem do jornal A é",porcentA)
    if b < c:
        print("A porcentagem do jornal B é",porcentB)
        print("A porcentagem do jornal C é",porcentC)
    else:
        print("A porcentagem do jornal C é",porcentC)
        print("A porcentagem do jornal B é",porcentB)
elif b < c:
    print("A porcentagem do jornal B é",porcentB)
    if a < c:
        print("A porcentagem do jornal A é",porcentA)
        print("A porcentagem do jornal C é",porcentC)
    else:
        print("A porcentagem do jornal C é",porcentC)
        print("A porcentagem do jornal A é",porcentA)
else:
    print("A porcentagem do jornal C é",porcentC)
    if a < b:
        print("A porcentagem do jornal A é",porcentA)
        print("A porcentagem do jornal B é",porcentB)
    else:
        print("A porcentagem do jornal B é",porcentB)
        print("A porcentagem do jornal A é",porcentA)
