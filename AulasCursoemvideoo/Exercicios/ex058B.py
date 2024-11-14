import random
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
comp = random.choice(lista)
acertou = False
t = 0
print('=-' * 20)
print('Escolhi um número de 0 a 10 !')
while not acertou:
    jogador = int(input('Qual número você acha que eu escolhi? '))
    t += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
           print('Mais...Tente denovo!')
        elif jogador > comp:
            print('Menos...Tente denovo!')
print('PARABÉNS!!! você acertou!')
print('Eu realmente tinha escolhido o número {} !'.format(comp))
print('Você acertou com {} tentativas!'.format(t + 1))
print('=-' * 20)
