pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f"{k} = {v} ")

estado = {'uf' : 'Rio de Janeiro','sigla': 'RJ'}
estado2 = {'uf' : 'São paulo','sigla': 'SP'}
brasil = list()
brasil.append(estado)
brasil.append(estado2)
print(brasil[0]['uf'])

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f"O campo {k} tem valor {v}.")

