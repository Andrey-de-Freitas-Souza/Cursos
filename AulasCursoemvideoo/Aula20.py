def cabecalho(msg):
    print('=-=' * 10)
    print(f"{msg:^30}")
    print('=-=' * 10)

cabecalho("SISTEMAS DE ALUNOS")
cabecalho("APRENDA PYTHON")
cabecalho("GUSTAVO GUANABARA")

def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos +=1
    print(valores)
valores = [7, 2, 5, 0, 4]
dobra(valores)


