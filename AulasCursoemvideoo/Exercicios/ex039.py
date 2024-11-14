import datetime
from datetime import date
ano = int(input('em que ano você nasceu? '))
atual = datetime.date.today().year
diferenca = atual - ano
if diferenca < 18:
    print('ainda faltam {} anos para você se alistar'.format(18 - diferenca))
elif diferenca > 18:
    print('já passaram {} anos do prazo do seu alistamento'.format(diferenca- 18))
elif diferenca == 18:
    print('Está na hora de se alistar!')
print('-------Fim--------')






