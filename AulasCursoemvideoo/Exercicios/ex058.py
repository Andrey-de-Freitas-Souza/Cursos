import random
import time

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = 'b'
comp = 'c'
t = 0

while num != comp:

    comp = random.choice(lista)

    print('=-' * 20)
    print('Escolhi um número de 0 a 10 !')
    time.sleep(1)
    num = int(input('Qual número você acha que eu escolhi? '))

    if comp == num:
        time.sleep(1)
        print('PARABÉNS!!! você acertou!')
        time.sleep(1)
        print('Eu realmente tinha escolhido o número {} !'.format(comp))
        print('Você acertou com {} tentativas!'.format(t + 1))

    else:
        t += 1
        time.sleep(1)
        print('Que pena , não foi dessa vez, tente denovo!')
        time.sleep(1)
        print('Tinha escolhido número {} e não o {} !'.format(comp, num))
print('=-' * 20)
