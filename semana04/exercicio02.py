valorPeca = float(input("Digite o valor da peça: "))
print ("1 - À vista.")
print ("2 - 2 vezes.")
print ("3 - 3 vezes.")
pagamento = int(input("Digite a forma de pagamento: "))
if pagamento == 1:
    print ("O valor R$",valorPeca,"será pago à vista")
elif pagamento == 2:
    parcelas = valorPeca / 2
    print ("As parcelas pagas seram do valor R$",parcelas)
elif pagamento == 3:
    parcelas = valorPeca / 3
    print ("As parcelas pagas seram do valor R$",parcelas)
else: 
    print ("Opção inválida!")