print ("A")
print ("B")
print ("C")
print ("D")
escolha = input("Digite sua resposta: ").upper()
if escolha == "A" or escolha == "C" or escolha == "D":
    print ("Resposta errada.")
elif escolha == "B":
    print ("Resposta correta.")
else:
    print ("Resposta inválida.")