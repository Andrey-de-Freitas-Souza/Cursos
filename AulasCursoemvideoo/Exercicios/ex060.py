n = int(input('Digite um valor :'))
f = n
print('O fatorial de {} é: '.format(n))
while f > 1:
    print(f, end=' x ')
    f -= 1
    r = n * f
    n = r
print('1 = {} '.format(r))

