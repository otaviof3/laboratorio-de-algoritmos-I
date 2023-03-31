valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
print ("1 - Soma.")
print ("2 - Subtração.")
print ("3 - Multiplicação.")
print ("4 - Divisão.")
calcular = int(input("Digite a operação a ser feita: "))
if calcular == 1:
    somar = valor1 + valor2
    print ("A soma dos valores é",somar)
elif calcular == 2:
    subtrair = valor1 - valor2
    print ("A subtração dos valores é",subtrair)
elif calcular == 3:
    multiplicar = valor1 * valor2
    print ("A multiplicação entre os valores é",multiplicar)
elif calcular == 4:
    dividir = valor1 / valor2
    print ("A divisão entre os valores é",dividir)
else:
    print("Opção inválida!")