p = int(input('Qual o primeiro termo da P.A? '))
r = int(input('Qual a razão da P.A? '))
t = 10
s = 0
q = 1
j = 0
while t > 0:
    t -= 1
    s = p + r
    print(p, end=' -> ')
    p = s

q = int(input('\nvocê quer saber mais quantos termos?'))
while j == 0:
    if q != 0:
        while q > 0:
            q -= 1
            s = p + r
            print(p, end=' -> ')
            p = s
    else:
        j += 1
    q = int(input('\nvocê quer saber mais quantos termos?'))
