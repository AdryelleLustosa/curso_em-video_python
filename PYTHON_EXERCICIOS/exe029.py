# programa pra dizer se foi multado ou não. A multa é 7,00 por km execdido

KM_PERMITIDO = float(80)
valor_multa = float(7)
velocidade = float(input('Qual a velocidade do carro? '))

if (velocidade > KM_PERMITIDO):
    multa = (velocidade-KM_PERMITIDO)*valor_multa
    print('Você excedeu o limite de velocida! O valor da suma multa é: {} reais'.format(multa))
else:
    print('Sua velocidade está dentro do limite permitido! Continue assim :)')