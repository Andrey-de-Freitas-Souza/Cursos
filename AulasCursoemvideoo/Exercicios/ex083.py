expr = str(input("Digite a expressão: "))
pilha = []
for simb in expr:
    if simb == "(":
        pilha.append('(')
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.appnd(')')
            break
if len(pilha) == 0:
    print("Sua expressão é válida!")
else:
    print("sua expressão está errada!")