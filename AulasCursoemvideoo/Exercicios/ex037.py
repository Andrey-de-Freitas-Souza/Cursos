num = int(input('Digite um valor: '))
e = int(input("""Digite 1 se você deseja converte-lo para binário,
2 se deseja converte-lo para octal e 
3 se deseja converte-lo para hexadecimal: """))
if e == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif e == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif e == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Por favor escolha uma das opções citadas.')
