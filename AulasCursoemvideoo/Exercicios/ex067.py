while True:
    n = int(input('Quer a tabuada de qual valor?'))
    print('-' * 30)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
