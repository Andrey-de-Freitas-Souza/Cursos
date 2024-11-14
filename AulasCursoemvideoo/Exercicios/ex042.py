r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('essas três retas formam um triangulo!')
    if r1 == r2 == r3:
        print('o triangulo formado será um tiângulo equilátero')
    elif r1 == r2 and r1 != r3 or r2 == r3 and r1 != r1 or r1 == r3 and r1 != r2 :
        print('o triangulo formado será um tiângulo isósceles')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('o triangulo formado será um tiângulo escaleno')
else:
    print('essas três retas não formam um triângulo')
