# while = enquanto
# então vau fivar repetindo até chegar na maçã

#   enquanto não maçã       #   while not apple
#       passo               #       passo
#   pega                    #   pega

#   enquanto não maçã       # while not apple:
#       se chão:            #   if chão:
#         passo             #       passo
#       se buraco:          #   if buraco:
#          pula             #       pula
#       se moeda:           #   if moeda:
#          pega             #       pega
#   pega                    # pega

#   c = 1
#   while c < 10:
#      print(c)
#      c = c + 1
#   print('Fim')

#   n = 1
#   while n != 0:
#      n = int(input('Digite um número: '))
#   print('fim')

#   r = 'S'
#   while r == 'S':
#      n = int(input('Digite um valor:'))
#      r = str(input('Quer continuar? [S/N] ')).upper()
#   print('fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} números pares e {} ímpares'. format(par, impar))
