n = 'a'
s = 0
q = 0
while n != 999:
    n = int(input('Digite um valor: [999 para parar] '))
    if n != 999:
        s += n
        q += 1
print('você digitou {} e a somatória desses números é {}'.format(q, s))
