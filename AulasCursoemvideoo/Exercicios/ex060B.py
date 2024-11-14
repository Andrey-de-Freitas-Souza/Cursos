n = int(input('Digite um número:'))
print('o fatorial de {} é: '.format(n))
for c in range(n, 1, -1):
    print(c, end=' x ')
    r = n * (c-1)
    n = r
print(' 1 = {}'.format(r))


#for( int c = 0; c< 10; c++)