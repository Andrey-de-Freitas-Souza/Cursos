n = int(input('Digite um número para saber sua tabuada: '))
print('{:=^30} '.format(' TABUADA DO {} '.format(n)))
for c in range(0 , 11):
    print('{} x {} = {}'.format(n, c, n*c))
print('{:=^30}'.format('Fim'))


