import datetime
from datetime import date

ano = int(input('em que ano o atleta nasceu? '))
atual = datetime.date.today().year
dif = atual - ano
print('O atleta tem {} anos.'.format(dif))
if dif <= 9:
    print(' o atleta está calssificado como MIRIM')

elif 9 < dif <= 14:
    print('o atleta está classificado como atleta INFANTIL')

elif 14 < dif <= 19:
    print('o atleta está classificado como JUNIOR')

elif 19 < dif <= 25:
    print('o atleta está classificado como SÊNIOR')

elif dif > 25:
    print('o atleta está classificado como MASTER')

print('--------Fim---------')
