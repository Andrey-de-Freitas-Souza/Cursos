m = 0                                           # média das idades
spm = 0                                         # soma para calcular a média
hv = 0                                          # nome do homem mais velho
i2 = 0                                          # para calcular qual é a maior idade
sm = 0                                          # para calcular o número de mulheres
for c in range(1, 5):                           #estrutura de repetição

    print('{}'.format('=-' * 20))               # cabeçalho

    n = str(input('Qual o seu nome?'))          # recebendo o nome

    i = int(input('Quantos anos você têm?'))    # recebendo a idade
    spm = spm + i                               # soma das idade para média
    m = spm / 4                                 # divindo a soma para obter a média

    print('[ 1 ] masculino')                    # opção de gênero
    print('[ 2 ] feminino')                     # opção de gênero
    s = int(input('Qual o seu gênero? '))       # recebendo o gênero

    if s == 1 and i > i2:                       # se a escolha for masculino e a idade for maior
        i2 = i                                  # i2 receberá o valor da idade que entrou
        hv = n                                  # e hv receberá o nome que entrou

    elif s == 2 and i < 21:                     # se não se escolha for feminino e a idade < 21
        sm = sm + 1                             # o número de mulheres aumenta 1

print(""" A média de idade dessas pessoas é de {} anos         
o homem mais velho desse grupo é o {} 
e existem {} mulheres com menos de 21 anos""".format(m, hv, sm))   # escrevendo os resultados

