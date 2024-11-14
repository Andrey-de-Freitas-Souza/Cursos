#help(print)
#print(input.__doc__)

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra ela na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=" ")
        c+=p
    print("Fim!")

def somar(a = 0,b = 0,c = 0):
    soma = a + b + c
    print(f"A soma vale {soma}")


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"A dentro vale {b}")
    print(f"A dentro vale {c}")

a = 5
teste(a)
print(f"A fora vale {a}")