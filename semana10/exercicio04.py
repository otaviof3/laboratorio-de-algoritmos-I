def parametro():
    temperatura = float(input("Digite a temperatura em °C: "))
    return temperatura
def fahren(temperatura):
    heit = (temperatura * 1.8) + 32
    return heit
def main():
    temperatura = parametro()
    heit = fahren(temperatura)
    print("A temperatura em °F é",heit)
main()