frase = str(input('Digite uma frase: ')).strip().upper()
frase2 = ''.join(frase.split())
inverso = ''
#inverso = frase2 [::-1]
for letra in range(len(frase2) - 1, -1, -1):
    inverso += frase2[letra]
print('o inverso de {} é {}'.format(frase2, inverso))
if inverso == frase2:
   print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')




