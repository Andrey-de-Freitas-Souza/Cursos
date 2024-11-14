from random import randint
import time
lista = list()
cont = 0

print("-" * 30)
print(f"          MEGA-SENA           ")
print("-" * 30)

qtd = int(input("Quantos jogos você quer qeu eu sorteie?"))

for c in range(0,qtd):
    while True:
        num = randint(1,60)
        if num  not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            cont = 0
            break
    lista.sort()
    print(f"Os números sorteados foram: {lista}")
    lista.clear()
    time.sleep(1)