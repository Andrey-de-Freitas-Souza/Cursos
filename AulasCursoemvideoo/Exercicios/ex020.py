from random import shuffle                          # importando shuffle do modulo rendom
a1 = input('Primeiro aluno: ')                      # recebendo o nome do primeiro aluno
a2 = input('Segundo aluno: ')                       # recebendo o nome do segundo aluno
a3 = input('Terceiro aluno ')                       # recebendo o nome do terceiro aluno
a4 = input('Quarto aluno:')                         # recebendo o nome do quarto aluno
lista = [a1, a2, a3, a4]                            # criando uma lista com os nomes dos alunos
shuffle(lista)                                      # embaralhando a lista
print('a ordem de aprensentação será:')             # dizendo qual será a ordem de apresentação
print(lista)
