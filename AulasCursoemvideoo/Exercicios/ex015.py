d = float(input('Quantos dias o carro foi alugado?'))   # recebendo a quantidade de dias
km = float(input('quantos KM foram rodados?'))          # recebendo a quantidade de Kms
v = (d * 60) + (km * 0.15)                              # calculando o valor total
print('o valor será de R${}'.format(v))

# dizendo o valor total
