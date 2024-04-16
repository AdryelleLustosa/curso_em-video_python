# Programa que converte metros em centimetro e milimetros 

valor_metros = float(input('Digite o valor em metros: '))
valor_centimetros = float(valor_metros*100)
valor_milimetros = float(valor_metros*1000)

print('O valor em metros: {} tem em centimetros: {} e em milimetros: {}'.format(valor_metros, valor_centimetros, valor_milimetros))