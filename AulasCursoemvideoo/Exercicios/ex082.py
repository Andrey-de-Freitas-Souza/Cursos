valores = []
pares = []
impares = []
while True:
    valores.append(int(input("Digite um valor:")))
    r = str(input("Deseja continuar? [S/N]"))
    if r in 'Nn':
        break

for i, v in enumerate(valores):
    if v % 2 ==0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print("=-" * 30)
print(f'A lista completa é {valores}')
print(f" A lista de pares é {pares}")
print(f" A lista de impares é {impares}")
