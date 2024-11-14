salario = float(input('qual é o salário? '))
if salario > 1250.00:
    aumento = (salario/100) * 10
    novo = aumento + salario
    print('o salário atualizado é de {} reias'.format(novo))
else:
    aumento = (salario / 100) * 15
    novo = aumento + salario
    print('o salário atualizado é de {} reias'.format(novo))
print('--------Fim--------')