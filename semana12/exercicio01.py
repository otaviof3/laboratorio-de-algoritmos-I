def criar(array):
    for n in range (1,11):
        array.append(n)
    return array
def inverso(array):
    for n in range (9,-1,-1):
        print (array[n])
def main():
    array = []
    array = criar(array)
    inverso(array)
main()
