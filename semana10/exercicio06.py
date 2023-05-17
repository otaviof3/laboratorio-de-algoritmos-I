def pesquisa (sim,nao):
    for i in range (0,20):
        resposta = input("Você aceita o lançamento do produto? Responda com Sim (S) ou Não (N): ").upper()
        if resposta == "S":
            sim = sim + 1
        elif resposta == "N":
            nao = nao + 1
    return sim, nao
def main():
    sim = 0
    nao = 0
    sim, nao = pesquisa (sim,nao)
    print("O total de pessoas que responderam sim é",sim)
    print("O total de pessoas que responderam não é",nao)
main()