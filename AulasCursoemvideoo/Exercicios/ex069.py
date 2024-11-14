contm = conth = contp = 0
while True:
    idade = 0
    sexo = ' '
    r = ' '
    print('-'*28)
    print('   CADASTRE UMA PESSOA')
    print('-' * 28)
    while idade <= 0:
        idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if idade >= 18:
        contp += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm += 1

    print('-' * 28)
    while r not in 'SN':
        r = str(input('Que continuar? [S/N] ')).strip().upper()

    if r in 'N':
        break

print('{:=^30}'.format(' FIM DO PROGRAMA '))
print(f"""O total de pessoas com mais de 18 anos é de {contp}
O total de homens que foram cadastrados foi de {conth}
E o total de mulheres com menos 20 anos cadastradas é de {contm}""")
