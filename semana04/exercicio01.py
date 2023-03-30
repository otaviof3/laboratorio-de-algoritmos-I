valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
if valor1 != valor2:
    if valor1 > valor2:
        print ("O valor",valor1,"é maior que o valor",valor2)
    elif valor2 > valor1:
        print ("O valor",valor2,"é maior que o valor",valor1)
elif valor1 == valor2:
    print("Os dois valores digitados são iguais")
