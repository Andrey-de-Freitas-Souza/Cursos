s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o valor {} valor: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('você digitou {} números pares e a soma total desses números é {}'.format(cont,s))



