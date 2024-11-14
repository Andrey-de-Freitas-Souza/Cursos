print('-' * 30)
print('LOJA BEM MAIS BARATO')
print('-' * 30)
total = mil = cont = 0
nbarato = ' '
while True:
    r = 'n'
    cont += 1
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()

    if preco > 1000:
        mil += 1
    if cont == 1:
        total = barato = preco
        nbarato = nome
    else:
        total += preco


    if preco < barato:
        barato = preco
        nbarato = nome

    if r in 'N':
        break

print('{:=^30}'.format(' FIM DO PROGRAMA '))
print(f"""O total da compra foi R${total}
temos {mil} produtos custando mais de R$1000.00
E o produto mais barato foi {nbarato} que custou {barato}""")
