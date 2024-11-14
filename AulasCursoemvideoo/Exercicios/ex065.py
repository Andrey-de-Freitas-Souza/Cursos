r = 's'
maior = menor = z = s = d = 0
while r not in 'N':
    print('=-' * 20)
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
    s += n
    d += 1
    if d == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n


print("""O maior número que você digitou foi o {}
 O menor número que você digitou foi o {} 
 E a média desses números é {}""".format(maior, menor, s / d))
