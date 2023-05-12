def ler (idades, maior, entre):
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso: "))
    idades = idades + idade
    if idade >= 18:
        maior = maior + 1
    if idade > 10 and idade < 30:
        entre = entre + 1
    return idades, maior, entre
def media(idades):
    print ("Média das idades:",idades / 7)
def quantidade (maior):
    print ("Quantidade de pessoas maiores de idade:",maior)
def porcentagem (entre):
    porcent = (entre * 100) / 7
    print ("A porcentagem de pessoas entre 10 e 30 anos é:",porcent)
def main ():
    idades = 0
    maior = 0
    entre = 0
    for i in range (0,7):
        idades, maior, entre = ler(idades, maior, entre)
    media(idades)
    quantidade(maior)
    porcentagem(entre)
main()
