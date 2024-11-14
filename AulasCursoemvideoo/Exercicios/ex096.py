def area(x,y):
    print(f"A área total do terreno é de {x*y:.2f}m.")

print("  CONTROLE DE TERRENOS")
print("--------------------------")
a = float(input("LARGURA (m): "))
b = float(input("ALTURA (m): "))

area(a,b)
