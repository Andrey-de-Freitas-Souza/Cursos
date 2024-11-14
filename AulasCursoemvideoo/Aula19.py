# DICIONÁRIOS
#---------------------------------------------------------
dados1 = dict()
dados = {'nome':'Pedro','idade':25}
print(dados['nome'])
dados['sexo'] = 'M'
print(dados['sexo'])
del dados['idade']
#---------------------------------------------------------
filmes = {'titulo' :'StarWars',
          'ano': 1977,
          'diretor':'GeorgeLucas'
}

print(filmes.values())
print(filmes.keys())
print(filmes.items())

for k, v in filmes.items():
    print(f"O {k} é {v}")
#---------------------------------------------------------
filme1 = {'titulo' :'StarWars',
          'ano': 1977,
          'diretor':'GeorgeLucas'
}

filme2 = {'titulo' :'Avengers',
          'ano': 2012,
          'diretor':'Joss Whedon'
}

filme3 = {'titulo' :'Matrix',
          'ano': 1999,
          'diretor':'Wachowski'
}
locadora =[]
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
print(locadora[0]['ano'])
#---------------------------------------------------------