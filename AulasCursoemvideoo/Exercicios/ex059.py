import time

r = 0
print('=-' * 20)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while r != 5:
    print(""" OPÇÕES:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Saber qual é maior
    [ 4 ] Escolher novos números
    [ 5 ] Sair do programa """)
    print('Os números escolhidos foram {} e {}'.format(n1, n2))
    r = int(input('Oquê você deseja fazer ?'))

    if r == 1:
        s = n1 + n2
        print('{} + {} = {}'.format(n1, n2, s))
        time.sleep(2)
        print('=-' * 20)

    if r == 2:
        m = n1 * n2
        print('{} x {} = {}'.format(n1, n2, m))
        time.sleep(2)
        print('=-' * 20)

    if r == 3 and n1 > n2:
        print('O maior número é o {}'.format(n1))
        time.sleep(2)
        print('=-' * 20)

    if r == 3 and n2 > n1:
        print('O maior número é o {}'.format(n2))
        time.sleep(2)
        print('=-' * 20)

    if r == 4:
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite um segundo novo valor: '))
        print('=-' * 20)

    if r == 5:
        print('{:=^40}'.format('Você saiu do programa'))
