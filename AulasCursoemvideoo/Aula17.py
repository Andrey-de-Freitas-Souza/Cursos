lanches = ["Hot-dog", "hamburguer", "refri", "sorvete", "coockie"]
lanches.pop(3)
del lanches[2]
if "coockie" in lanches:
    lanches.remove("coockie")
print(lanches)

valores = list(range(4,11))

valores2 = [8, 2, 5, 4, 9, 3, 0]
valores2[2] = 1
valores2.append(7)
valores2.insert(3, 23)
valores2.pop()
valores2.pop(3)
valores2.sort(reverse= True)
print(valores2)