print('=' * 30)
print("        BANCO DREY'S ")
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
c = v = d = u = 0
resto = resto2 = resto3 = resto4 = 0
while True:
    if valor >= 50:
        while valor >= 50:
            resto = valor - 50
            valor -= 50
            c += 1
    if valor >= 20:
        while valor >= 20:
            resto2 = resto - 20
            valor -= 20
            v += 1
    if valor >= 10:
        while valor >= 10:
            resto3 = resto2 - 10
            valor -= 10
            d += 1
    if valor >= 1:
        while valor >= 1:
            resto4 = resto3 - 1
            valor -= 1
            u += 1
    if valor == 0:
        break

if c > 0:
    print(f'Total de {c} cédulas de [R$50]')
if v > 0:
    print(f'Total de {v} cédulas de [R$20]')
if d > 0:
    print(f'Total de {d} cédulas de [R$10]')
if u > 0:
    print(f'Total de {u} cédulas de [R$1]')

print('=' * 30)
print("Volte sempre ao BANDO DREY'S! Tenha um bom dia!")
