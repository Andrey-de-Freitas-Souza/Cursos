print('{:=^40}'.format(' LOJAS FREITAS '))
p = float(input('Valor das compras: '))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em 2 vezes no cartão
[ 4 ] 3x ou mais no cartão""")
r = int(input('Qual é a opção?'))
d1 = p - (p / 100 * 10)
d2 = p - (p / 100 * 5)
j = p + (p / 100 * 20)
if r == 1:
    print('o valor das compras será de R${} com essa forma de pagamento'.format(d1))
elif r == 2:
    print('o valor das compras será de R${} com essa forma de pagamento'.format(d2))
elif r == 3:
    parcela = p / 2
    print('o valor das compras será de R${} com essa forma de pagamento,'.format(p))
    print('a sua compra será parcelada em 2x de R${}'.format(parcela))
elif r == 4:
    par = int(input('Quantidade de parcelas: '))
    print('o valor das compras será de R${} com essa forma de pagamento'.format(j))
    print('a sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(par,j / par))
else:
    print('\033[0;31mOPÇÃO INVÁLIDA. Tente novamente!')

