#------------------------------------------------------------
# laço c no intervalo(1,10)  >>>   # for c in range(1,10)
#   passo                    >>>   #   passo
#pega                        >>>   #pega
#-------------------------------------------------------------
# laço c no intervalo(0,3)  >>>   # for c in range(0,3)
#   passo                   >>>   #   passo
#   pula                          #   pula
#passo                            #passo
#pega                             #pega
#------------------------------------------------------------
# laço c no intervalo(0,3)  >>>   # for c in range(0,3)
#   se moeda                      #     if coin
#       pega                      #         pega
#   passo                   >>>   #     passo
#   pula                          #     pula
#passo                            #passo
#pega                             #pega
#------------------------------------------------------------


#for c in range(0, 6):
#    print('oi')
#print('oi')

#for c in range(0, 10 , 2):
#    print(c)
#print('fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor : '))
    s += n
print('o somatório de todos os valores foi {}'.format(s))






