def parametro():
    numero = int(input("Digite um número: "))
    return numero
def primo(numero,primos):
    if numero < 2:
        return False
    else:
        for i in range (1,numero + 1):
            if numero % i == 0:
                primos = primos + 1
        if primos == 2:
            return True
        else:
            return False
def main():
    primos = 0
    numero = parametro()
    resultado = primo(numero,primos)
    print (resultado)
main()