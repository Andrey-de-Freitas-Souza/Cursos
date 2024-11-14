nome = input('qual o seu nome? ')                       # recebendo um nome
separado = nome.split()                                 # separando o nome
print('Seu primeiro nome é: {}'.format(separado[0]))    # dizendo o primeiro nome
print('seu ultimo nome é: {}'.format(separado[-1]))     # dizendo o último nome
