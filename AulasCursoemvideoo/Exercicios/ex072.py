lista =('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quize', 'desesseis', 'desesete', 'dezoito',
        'dezenove', 'vinte')
r = -1
while r < 0 or r > 20:
    r = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {lista[r]}')

