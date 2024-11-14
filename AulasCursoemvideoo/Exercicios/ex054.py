import datetime
atual = datetime.date.today().year
ma = 0
me = 0
for c in range(1, 8):
    n = int(input('Em que ano você nasceu? '))
    if atual - n >= 21:
        ma += 1
    else:
        me += 1
print('o total de pessoas que já atingiram a maioridade é {}'.format(ma))
print('o total de pessoas que não atingiram a maioridade é {}'.format(me))

