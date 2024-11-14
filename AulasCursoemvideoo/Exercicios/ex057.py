r = 'e'
while r not in 'MF':
    r = str(input('Qual o seu sexo? [F/M] ')).upper().strip()
    if r not in 'MF':
        print('Digite uma opção mencionada.')
print('Obrigado!')
