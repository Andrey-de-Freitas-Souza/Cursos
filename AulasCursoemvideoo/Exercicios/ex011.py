b = float(input('Qual a largura da parede?'))   # recebendo o valor da largura da parede
h = float(input('Qual a altura da parede?'))    # recebendo o valor da altura da parede
a = b*h                                         # cálculo da área total da parede
print('A área da parede é de {:.3} m2 e será necessário {:.3} litros de tinta'.format(a, a/2))

# dizendo quantos baldes de tinta serão nescessários
