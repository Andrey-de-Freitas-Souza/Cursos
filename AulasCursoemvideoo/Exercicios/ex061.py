p = int(input('Qual o primeiro termo da P.A? '))
r = int(input('Qual a razão da P.A? '))
t = 10
s = 0
while t > 0:
    t -= 1
    s = p + r
    print(p, end=' -> ')
    p = s
print('Fim')
