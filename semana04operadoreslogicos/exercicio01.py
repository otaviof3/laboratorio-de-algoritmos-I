nome = input("Informe seu nome: ")
salario = float(input("Informe seu salário: "))
tempo = int(input("Informe seu tempo de serviço: "))
if tempo >= 5 and salario <= 2000.00:
    aumento = salario + (salario * 0.1)
    print("Senhor",nome,"seu salário de",salario,"poderá receber um aumento de 10%, tornando-se em",aumento)
else:
    aumento = salario + (salario * 0.05)
    print("Senhor",nome,"seu salário de",salario,"poderá receber um aumento de 5%, tornando-se em",aumento)
