morango = float(input("Quantidade de morangos (kg): "))
macas = float(input("Quantidade de maçãs (kg): "))
if morango > 5:
    valorMorango = morango * 2.20
else:
    valorMorango = morango * 2.50
if macas > 5:
    valorMaca = macas * 1.50
else:
    valorMaca = macas * 1.80
kgTotal = morango + macas
valorTotal = valorMorango + valorMaca
if kgTotal > 8 or valorTotal > 25.00:
    valorDesconto = valorTotal - (valorTotal * 0.1)
    print("O valor a ser pago é",valorDesconto)
else:
    print("O valor a ser pago é",valorTotal)