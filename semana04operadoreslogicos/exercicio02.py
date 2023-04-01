lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
lado3 = float(input("Digite o valor do terceiro lado do triângulo: "))
if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Digite um valor diferente de zero, ou positivo.")
elif (lado1 + lado2) < lado3 or (lado2 + lado3) < lado1 or (lado1 + lado3) < lado2:
    print("Um triângulo não pode ser formado.")
elif lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("O triângulo formado é equilátero.")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("O triângulo formado é isósceles.")
else:
    print("O triângulo formado é escaleno.")