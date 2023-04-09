moradores = 0
moradoresA = 0
moradoresB = 0
moradoresC = 0
while moradores < 10:
    elevador = input("Informe o elevador (A, B ou C) que utiliza com mais frequência: ").upper()
    if elevador == "A":
        moradoresA = moradoresA + 1
    elif elevador == "B":
        moradoresB = moradoresB + 1
    elif elevador == "C":
        moradoresC = moradoresC + 1
    moradores = moradores + 1
qMoradoresA = moradoresA / moradores
qMoradoresB = moradoresB / moradores
qMoradoresC = moradoresC / moradores
porcentagemA = qMoradoresA * 100
porcentagemB = qMoradoresB * 100
porcentagemC = qMoradoresC * 100
print ("O número de pessoas que utliza o elevador A é",moradoresA,"e sua porcentagem",porcentagemA)
print ("O número de pessoas que utliza o elevador B é",moradoresB,"e sua porcentagem",porcentagemB)
print ("O número de pessoas que utliza o elevador C é",moradoresC,"e sua porcentagem",porcentagemC)