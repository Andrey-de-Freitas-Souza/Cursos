print('=-'*30)
print('sequência de fibonatti')
print('=-'*30)
n = int(input('quantos termos você quer que eu mostre? '))
t1 = 0
t2 = 1
print(' {} -> {} '.format(t1, t2), end='')
cont = 3
while cont <= n:
    cont += 1
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
print('\n FIM')