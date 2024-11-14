import moeda

p = float(input("Digite o preço: "))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}")
print(f"Aumentado 10%, temos {moeda.aumentar(p,10,True)}")
print(f"diminuindo 15% temos {moeda.diminuir(p,15,True)}")