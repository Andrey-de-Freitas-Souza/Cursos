import random
from time import sleep
def sorteia():
    lista = list()
    sorteio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for c in range(0,5):
        num = random.choice(sorteio)
        lista.append(num)
        print(num, end=" ")
        sleep(0.3)
    return lista
def somaPar(lista):
    somaP = 0
    for n in lista:
        if n % 2 == 0:
            somaP += n
    print(f"\nA soma dos valores pares sorteados é {somaP}")
print("Sorteando 5 valores da lista")
somaPar(sorteia())









