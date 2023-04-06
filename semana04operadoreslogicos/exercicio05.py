print("Interrogatório: Responda as seguintes perguntas com 1 para Sim ou 2 para Não.")
pergunta1 = input("Telefonou para a vítima? ")
if pergunta1 == "1":
    sim1 = 1
else:
    sim1 = 0
pergunta2 = input("Esteve no local do crime? ")
if pergunta2 == "1":
    sim2 = sim1 + 1
else:
    sim2 = sim1 + 0
pergunta3 = input("Mora perto da vítima? ")
if pergunta3 == "1":
    sim3 = sim2 + 1
else:
    sim3 = sim2 + 0
pergunta4 = input("Devia para a vítima? ")
if pergunta4 == "1":
    sim4 = sim3 + 1
else:
    sim4 = sim3 + 0
pergunta5 = input("Já trabalhou com a vítima? ")
if pergunta5 == "1":
    sim = sim4 + 1
else:
    sim = sim4 + 0
if sim == 5:
    print("Pessoa classificada como Assassino.")
elif sim >= 3:
    print("Pessoa classificada como Cúmplice.")
elif sim == 2:
    print("Pessoa classificada com Suspeita.")
else:
    print("Pessoa classificada como Inocente.")