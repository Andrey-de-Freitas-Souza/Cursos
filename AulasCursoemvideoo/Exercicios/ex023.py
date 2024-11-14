numero = input('escolha um número de 0 a 9999: ')       # recebendo o número
numerosep = numero.split()                              # separando o número
print('unidade: {}'.format(numerosep[0][3]))           # dizendo a unidade
print('dezena: {}'.format(numerosep[0][2]))            # dizendo a dezena
print('centena: {}'.format(numerosep[0][1]))           # dizendo a centena
print('milhar: {}'.format(numerosep[0][0]))            # dizendo o milhar
