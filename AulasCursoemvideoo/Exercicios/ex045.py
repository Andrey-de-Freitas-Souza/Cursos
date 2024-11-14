import random
import time

lista = ['Pedra','Papel','Tesoura',]
comp = random.choice(lista)

print('Vamos jogar jonkenpô?')

time.sleep(2)

print("""Escolha entre:
[ 1 ] PEDRA 
[ 2 ] PAPEL
[ 3 ] TESOURA
""")
r = int(input('Escolha sua jogada: '))

if r == 1:
    r = 'Pedra'

elif r == 2:
    r = 'Papel'

elif r == 3:
    r = 'Tesoura'

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)

print('{}'.format('=-' *12))
print('Computador jogou {}'.format(comp))
print('Jogador jogou {}'.format(r))
print('{}'.format('=-' *12))

time.sleep(1)

# empate

if r == 'Pedra' and comp =='Pedra' or r == 'Papel' and comp =='Papel' or r == 'Tesoura' and comp =='Tesoura':
    print('EMPATE')

#usuário ganhando

elif r == 'Pedra' and comp == 'Tesoura':
    print('JOGADOR VENCEU')

elif r == 'Papel' and comp == 'Pedra':
    print('JOGADOR VENCEU')

elif r == 'Tesoura' and comp == 'Papel':
    print('JOGADOR VENCEU')

#Computador ganhando

elif comp == 'Pedra' and r == 'Tesoura':
    print('COMPUTADOR VENCEU')

elif comp == 'Papel' and r == 'Pedra':
    print('COMPUTADOR VENCEU')

elif comp == 'Tesoura' and r == 'Papel':
    print('COMPUTADOR VENCEU')
