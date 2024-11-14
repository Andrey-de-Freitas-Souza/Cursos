print('=' * 30)
print("        BANCO DREY'S ")
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
c = valor // 50
v = (valor - (c * 50)) // 20
d = (valor - ((c * 50) + (v * 20))) // 10
u = (valor - ((c * 50) + (v * 20) + (d * 10))) // 1
print(f"""Total de {c} cédulas de [R$50]
Total de {v} cédulas de [R$20]
Total de {d} cédulas de [R$10]
Total de {u} cédulas de [R$1]
""")
print('=' * 30)
print("Volte sempre ao BANDO DREY'S! Tenha um bom dia!")
