num = (int(input('Digite o primeiro valor:')),
        int(input('Digite o segundo valor:')),
        int(input('Digite o terceiro valor:')),
        int(input('Digite o quarto valor:')))

print(f"Você digitou os valores {num}")
print(f" O valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"A primeira posição que o número 3 apareceu"
          f" foi na {num.index(3) + 1} posição")
else:
    print("O valor 3 não foi digitado")
print("os valores pares digitados foram:")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")

