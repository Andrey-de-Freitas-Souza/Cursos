ano = int(input('Digite uma ano, para saber se ele é bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print(' o ano {} não é bissexto'.format(ano))
print('--------Fim---------')
