print ("Categorias: A, B, C, D e E:")
categoria = input("Digite o tipo de sua carteira: ").upper()
if categoria == "A":
    print ("Você pode dirigir motos e triciclos.")
elif categoria == "B":
    print ("Você pode dirigir carros de passeio.")
elif categoria == "C":
    print ("Você pode dirigir veículos de carga acima de 3,5 ton.")
elif categoria == "D":
    print ("Você pode dirigir veículos com mais de 8 passageiros.")
elif categoria == "E":
    print ("Você pode dirigir veículos com unidade acoplada acima de 6 ton.")
else:
    print ("Solicitação inválida!")