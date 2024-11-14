v = int(input('Qual é o valor da casa ? '))
s = int(input('Qual o sálario ? '))
a = int(input('Em quantos anos você pretende pagar a casa? '))
p = v / (a * 12)
if p > (s / 100) * 30:
    print('Desculpe, mas o empréstimo foi negado. ')
else:
    print('O empréstimo foi aprovado. ')

