def somaImposto():
    taxaImposto = int(input("Digite a taxa de imposto(%): "))
    custo = float(input("Digite o custo do item: "))
    imposto = (custo * taxaImposto) / 100
    custo = custo + imposto
    return custo
def main():
    custo = somaImposto()
    print ("O custo após imposto é",custo)
main()