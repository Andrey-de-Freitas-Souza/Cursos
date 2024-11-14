import random
print('=-' * 15)
print('  VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
cont = 0
while True:
    comp = random.randint(0, 10)
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()
    if escolha in 'P':
        escolha = 'par'
    else:
        escolha = 'impar'
    s = jogador + comp
    print('-' * 30)
    if s % 2 == 0:
        resultado = 'DEU PAR'
    else:
        resultado = 'DEU ÍMPAR'
    print(f'Você jogou {jogador} e o computador {comp}. Total de {s}, {resultado}')
    print('-' * 30)
    if s % 2 == 0 and escolha == 'par':
        print('Você VENCEU!\nVamos jogar novamente...')
        print('=-' * 15)
        cont += 1
    elif s % 2 != 0 and escolha == 'par':
        print('Você PERDEU !')
        print('=-' * 15)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break
    elif s % 2 != 0 and escolha == 'impar':
        print('Você VENCEU!\nVamos jogar novamente...')
        print('=-' * 15)
        cont += 1
    elif s % 2 == 0 and escolha == 'impar':
        print('Você PERDEU !')
        print('=-' * 15)
        print(f'GAME OVER!Você venceu {cont} vezes.')
        break
