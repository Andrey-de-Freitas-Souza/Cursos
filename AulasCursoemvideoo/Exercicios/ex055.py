p2 = 0
m2 = 0
for c in range(1, 6):
    p = float(input('Qual o seu peso? '))
    if c == 1:
        p2 = p
        m2 = p
    else:
        if p > p2:
            p2 = p

        if p < m2:
            m2 = p

print('O maior peso resgistrado foi de {} Kg.'.format(p2))
print('O menor peso registrado foi de {} Kg.'.format(m2))