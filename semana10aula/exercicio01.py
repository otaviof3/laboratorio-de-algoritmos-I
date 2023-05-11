def receberMetros():
    metros = float(input("Digite o valor em metros: "))
    return metros
def decimetros(metros):
    metros = metros * 10
    print (metros,"decímetros")
def centimetros(metros):
    metros = metros * 100
    print (metros,"centímetros")
def milimetros(metros):
    metros = metros * 1000
    print (metros,"milímetros")
def main():
    metros = receberMetros()
    decimetros(metros)
    centimetros(metros)
    milimetros(metros)
main()
