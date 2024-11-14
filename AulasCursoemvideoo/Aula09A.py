frase =  'Curso em Vídeo Python'
#print(frase[9:21:])
#print(frase[9::3])
#print(frase[9:15:2])
#print(len(frase))               # (len) conta quantos caracteres existem
#print(frase.count('o'))         # (count) conta quantos caracteres mencionados há na frase
#print(frase.count('o',0,13))
#print(frase.find('deo'))
#print(frase.find('Android'))    #se não ouver a str mencionada o valor dado será (-1)
#print('curso'in frase)          # o operador (in) indicara se o str mnecionada existe na str completa

#transformação
#print(frase.replace('python','android'))  #substitui as palavras
#frase = frase.replace('Python','android')
#print(frase)

#print(frase.upper())                      #coloca a frase toda em maiusculas
#print(frase.lower())                      #coloca a frase toda em minuscula
#print(frase.capitalize())                 #coloca apenas a primeira letra em maiusculo
#print(frase.title())                       #coloca todas as iniciais em maiusculo
#print(frase.strip()) #variaçoes rstrip lstrip #remove os epaços a mais do inicio e do final da str

#divisão
#print(frase.split())
#dividido= frase.split()
#print(dividido[0])

#junção
#print('-'.join(frase.split()))


# o print pode ser usado com 3 aspas duplas para strs longas assim n é nescessário utilizar print em todas as linhas
#print("""xxxxxxxxxxxxxx""")