from time import sleep
def maior(*num):
    maior = 0
    for n in num:
        if n > maior:
            maior = n
    print("=-=" * 10)
    print(f"Analisando os valores Passados...")
    for n in num:
        print(n, end=', ')
        sleep(0.3)
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor que eu recebi foi {maior}")

maior(4,6,2,8,236,89,3)
maior(4,7,2,6,8,9,5,7)
maior(2,6,86,3,6,8,9)