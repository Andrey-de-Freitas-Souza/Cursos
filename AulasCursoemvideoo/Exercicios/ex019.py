import random                       # importando random
a1 = input('Primeiro aluno: ')      # recebendo nome do primeiro aluno
a2 = input('Segundo aluno: ')       # recebendo nome do segundo aluno
a3 = input('Terceiro aluno ')       # recebendo nome do terceiro aluno
a4 = input('Quarto aluno:')         # recebendo o nome do quarto aluno
lista = [a1, a2, a3, a4]            # criando uma lista com o nome dos alunos
print('o escolhido foi {}'.format(random.choice(lista)))    # dizendo qual aluno foi escolhido
