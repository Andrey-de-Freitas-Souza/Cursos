distancia = int(input('Qual foi a distância da viagem? '))
if distancia < 200:
    valor = distancia * 0.50
    print('o valor da passagem é de {} reais'.format(valor))
else:
    valor = distancia * 0.45
    print('o valor da passagem é de {} reais'.format(valor))
print('Faça uma boa viagem!')