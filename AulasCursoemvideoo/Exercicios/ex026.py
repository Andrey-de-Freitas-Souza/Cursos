frase = input('escreva uma frase: ')        # recebendo uma frase
frase2 = frase.upper().strip()              # colocando a frase em maiúsculo e tirando espaços
print('a letra A aparece {} vezes na sua frase '.format(frase2.count('A')))     # contando quantos A
print('a primeira letra A aparece na posição: {} '.format(frase2.find('A')+1))  # posição primeiro A
print('a ultima letra A aparece na posição: {} '.format(frase2.rfind('A')+1))  # posiçao do último A
