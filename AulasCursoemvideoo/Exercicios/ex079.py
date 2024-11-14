listanum = []
while True:
    n = int(input("Digite um valor:"))
    if n not in listanum:
        listanum.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar...")
    r = str(input("Deseja continuar? [S/N]"))
    if r in 'Nn':
        break
listanum.sort()
print(listanum)