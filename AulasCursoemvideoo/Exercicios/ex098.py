from time import(sleep)
def contador(inicio,fim,passo):
    if passo == 0:
        passo = 1
    if fim < inicio:
        if passo > 0:
            passo = 0 - passo
            fim -= 1
        else:
            fim -= 1
    else:
        fim += 1

    print("=-"* 20)
    print("Contagem de 1 até 10 de 1 em 1")
    print("=-" * 20)
    for c in range(1,11):
        print(f"{c} ", end="")
        sleep(0.3)
    print()
    print("=-" * 20)
    print("Contagem de 1 até 10 de 2 em 2")
    print("=-" * 20)
    for c in range(1,11,2):
        print(f"{c} ", end="")
        sleep(0.3)
    print()
    print("=-" * 20)
    print(f"Contagem de {inicio} até {fim+1} de {passo} em {passo}")
    print("=-" * 20)
    for c in range(inicio,fim,passo):
        print(f"{c} ", end="")
        sleep(0.3)

inicio = int(input("Qual será o começo da contagem? "))
fim = int(input("Qual será o fim da contagem? "))
passo = int(input("De quanto em quanto eu devo contar? "))
contador(inicio,fim,passo)