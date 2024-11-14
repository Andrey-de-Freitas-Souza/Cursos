def fatorial(num, show = False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show and c > 1:
            print(f, end=" ")
    return f

n = int(input("Digite um número: "))
print(f"\nO fatorial de {n} é igual a {fatorial(n, True)}")