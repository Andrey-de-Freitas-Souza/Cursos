p = int(input('Qual o primeiro termo da P.A? '))
r = float(input('Qual a razão da P.A? '))
for c in range(1, 11,):
    an = p + (c - 1) * r
    print(an, end=' -> ')
