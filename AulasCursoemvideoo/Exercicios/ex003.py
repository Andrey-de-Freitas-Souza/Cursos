n1 = int(input('digite o primeiro valor:'))  # recebendo primeiro valor
n2 = int(input('digite o segundo valor :'))  # recebendo o segundo valor
s = n1 + n2                                  # soma dos valores
cores = {'limpa': '\033[m',                 # lista de cores
         'vermelho': '\033[0;31m',
         'azul': '\033[0;34m',
         'verde': '\033[0;32m'}

print(' a soma entre {}{}{} e {}{}{} vale {}{}{}'.format(cores['vermelho'], n1, cores['limpa'], cores['azul'], n2, cores['limpa'], cores['verde'], s, cores['limpa']))

# dando o resultado
