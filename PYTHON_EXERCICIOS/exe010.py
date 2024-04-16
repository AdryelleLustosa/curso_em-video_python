# Programa para converter em dolar

moeda_real = float(input('Quanto você tem? '))
moeda_dolar = float(moeda_real / 3.27)

print('Com {} reais você pode comprar {:.2f} dolares'.format(moeda_real, moeda_dolar))