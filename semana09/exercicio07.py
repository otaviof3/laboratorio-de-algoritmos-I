def conversao(hora):
    if hora > 12 and hora < 24:
        hora = hora - 12
        notacao = "PM"
    elif hora < 12 and hora >= 0:
        notacao = "AM"
    elif hora == 12:
        notacao = "PM"
    return hora, notacao
def saida(hora,minutos,notacao):
    if notacao == "AM":
        print(hora,":",minutos,"AM")
    else:
        print(hora,":",minutos,"PM")
def main():
    hora = int(input("Valor de 0 a 23 para hora: "))
    minutos =  int(input("Valor de 0 a 59 para minutos: "))
    hora, notacao = conversao(hora)
    saida(hora,minutos,notacao)
main()