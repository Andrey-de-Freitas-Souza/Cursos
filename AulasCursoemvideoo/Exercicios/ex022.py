nome = input("qual o seu nome?")                                # recebendo o nome
print('Seu nome em maiusculo é : {} '.format(nome.upper()))     # dizendo o nome em maiúsculo
print('Seu nome em minusculo é : {} '.format(nome.lower()))     # dizendo o nome em minúsculo
print('você escreveu seu nome com {} caracteres '.format(len(nome)))   # dizendo quantos caracteres
nome2 = ''.join(nome.strip().split())                           # juntando o nome
print('Seu nome sem espaços tem {} caracteres'.format((len(nome2))))    # dizendo quantas letras
nomesep = nome.split()                                          # separando o nome
print('seu primero nome é : {} '.format(nomesep[0]))            # dizendo o primeiro nome
print('seu primero nome tem {} letras'.format(nome.find(' ')))  # dizendo quantas letras p nome
