valores = []
while True:
    valores.append(int(input("Digite um valor:")))

    r = str(input("Deseja continuar? [S/N]"))
    if r in 'Nn':
        break
print("-=" * 30)
print(f"Você digitou {len(valores)} elementos")
valores.sort(reverse=True)
print(f" Os valores em ordem decreceste são {valores}")
if 5 in valores:
    print(" O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")
