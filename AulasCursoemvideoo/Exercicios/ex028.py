import random                                         # importando random
from time import sleep                                # importando sleep do time
lista = [0, 1, 2, 3, 4, 5]                                 # criando uma lista com os números de 0 a 5
n = random.choice(lista)                              # escolhendo um número da lista
print('vou escolher um número entre 0 e 5 ! ')        # informação ao usuário
sleep(2)                                              # esperando 2 seg
num = int(input('qual número você acha que eu escolhi? '))  # recebendo resposta do usuário
print('PROCESSANDO...')                               # informação ao usuário
sleep(3)                                              # esperando 3 seg
if n == num:                # se o número escolhido pelo usuário for igual a resposta do usuário
    print('PARABÉNS!!! você acertou!')      # escreva ....
else:                                       # senão
    print('Que pena , não foi dessa vez, tente denovo!')    # escreva ...
    print('o número que escolhi foi o {} e não o {} !'.format(n, num))  # dizendo qual numero escolhido
