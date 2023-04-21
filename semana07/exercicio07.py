numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
while numero2 < numero1:
    print("Erro: o primeiro valor deve ser menor que o segundo")
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
for x in range (numero1 + 1,numero2):
    if x% 2 == 0:
        print(x)