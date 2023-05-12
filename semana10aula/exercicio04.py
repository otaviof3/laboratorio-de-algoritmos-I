def entrevista (a, b, c):
    elevador = input("Qual elevador (A, B ou C): ").upper()
    if elevador == "A":
        a = a + 1
    elif elevador == "B":
        b = b + 1
    elif elevador == "C":
        c = c + 1
    return a, b, c
def informacoes(a, b, c):
    print("Pessoas que usam o Elevador A:",a)
    print("Pessoas que usam o Elevador B:",b)
    print("Pessoas que usam o Elevador C:",c)
    porcentA = (a * 100) / 10
    porcentB = (b * 100) / 10
    porcentC = (c * 100) / 10
    print("Porcentagem das pessoas que usam o Elevador A:",porcentA)
    print("Porcentagem das pessoas que usam o Elevador B:",porcentB)
    print("Porcentagem das pessoas que usam o Elevador C:",porcentC)
def main():
    a = 0
    b = 0
    c = 0
    for i in range (0,10):
        a, b, c = entrevista(a, b, c)
    informacoes(a, b, c)
main()
