from math import pow, sqrt                         # importando pow() e sqrt() da biblioteca math
c1 = float(input('comprimento do cateto oposto:'))      # recebendo o valor do cateto oposto
c2 = float(input('comprimento do cateto adjacente:'))   # recebendo o valor do cateto adjacente
i = sqrt(pow(c1, 2)+pow(c2, 2))                         # calculando o valor da hipotenusa
print('o tamanho da hipotenusa é {}'.format(i))         # dizendo o valor da hipotenusa
