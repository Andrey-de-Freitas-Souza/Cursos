n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('a média do aluno foi de {}'.format(m))
if m < 5:
    print('O aluno foi reprovado.')
elif 5 <= m < 7:
    print('O aluno ficou de recuperação.')
elif m >= 7:
    print('O aluno foi aprovado.')
print('-------fim---------')
