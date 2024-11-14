vel = int(input('qual era a velocidade do carro? '))        # recebendo a velocidade do carro
if vel > 80:                                        # se a velocidade for maior que 80
    multa = (vel - 80) * 7                          # cálculo da multa
    print("""você excedeu o limite de velocidade    
então foi multado no valor de {} reais.""".format(multa))  # escreva o valor da multa
print('tenha sempre responsabilidade no trânsito!')  # escreva ...
