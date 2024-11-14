import datetime
def voto(nasc):
    idade = datetime.date.today().year - nasc
    msg = f"Com {idade} anos o voto é NEGADO."
    if 16 <= idade < 18:
        msg = f"Com {idade} anos o voto é OPCIONAL"
    if idade >= 18:
        msg = f"Com {idade} anos o voto é OBRIGATÓRIO"
    return msg

ano = int(input("Em que ano você nasceu?"))
print(voto(ano))