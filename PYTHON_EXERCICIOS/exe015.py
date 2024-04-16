# Carro Alugado

dias_alugado = int(input('Por quantos dias lugou o carro? '))
km_rodados= float(input('Por quantos KM rodou? '))
valordiaria = float(dias_alugado * 60)
valor_km = float(km_rodados*0.15)

print('O valor em diarias do seu carro foi: {} o valor me KM foi {}, portanto, o valor total é: {}'.format(valordiaria,valor_km, (valordiaria+valor_km)))