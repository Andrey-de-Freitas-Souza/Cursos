p = float(input('Qual o seu peso?'))
a = float(input('qual a sua altura? '))
imc = p / (a ** 2)
if imc < 18.5:
    print('você está abaixo do peso ideal para sua altura.')
elif 18.5 <=imc <= 25:
    print('O seu peso é ideal para a sua altura.')
elif 25 <=imc <=30:
    print('você está com sobrepeso.')
elif 30 <=imc <=40:
    print('você está com obesidade.')
elif imc > 40:
    print('você está com obesidade mórbida.')
