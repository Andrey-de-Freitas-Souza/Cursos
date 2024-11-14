matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaCol3 = maior = 0
for i in range(0,3):
    for c in range(0,3):
        matriz[i][c] = int(input(f"Digite o valor para [{i}] [{c}]"))
        if matriz[i][c] % 2 == 0:
            somaPar += matriz[i][c]
        if c == 2:
            somaCol3 += matriz[i][c]
        if i == 1:
            if matriz[i][c] > maior:
                maior = matriz[i][c]

print("=-" * 30)
for i in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[i][c]:^5}]", end="")
    print()
print("=-" * 30)
print(f"A soma dos valores pares é {somaPar}")
print(f"A soma dos valores da terceira coluna é {somaCol3}")
print(f"O maior valor da segunda linha é {maior}")