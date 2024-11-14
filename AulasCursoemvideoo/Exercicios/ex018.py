import math                                             # importand math
an = float(input('digite o angulo que você deseja:'))   # recebendo o valor do angulo
c = math.cos(math.radians(an))                          # calculando o cosseno
s = math.sin(math.radians(an))                          # calculando o seno
tg = math.tan(math.radians(an))                         # calculando a tangente
print('o angulo de {} tem o SENO de {:.2f} COSSENO {:.2f} e TANGENTE DE {:.2f} '.format(an, s, c, tg))

# dizendo os valores do seno cosseno e tangente
