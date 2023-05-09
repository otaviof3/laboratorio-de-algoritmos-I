def lerLaranjas():
    total = int(input("Total de laranjas: "))
    return total
def valorLaranjas(total):
    if total > 12:
        valor = total * 0.25
    else:
        valor = total * 0.40
    return valor
def main():
    total = lerLaranjas()
    valor = valorLaranjas (total)
    print ("O valor total é",valor)
main()