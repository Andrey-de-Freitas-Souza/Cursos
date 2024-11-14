cont = s = 0
while True:
    n = int(input('Digite um valor: [999] para parar'))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Você digitou {cont} números e a somatória\ndos valores digitados é {s} ')
