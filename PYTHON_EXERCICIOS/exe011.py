# Calcular area e saber quanto de tinta precisa

largura_parede = float(input('Qual a largura da parede? '))
altura_parede = float(input('Qual a altura da parede: '))
area = float(largura_parede*altura_parede)
tinta = float(area/2)

print('Para a area de {} metros, serão necessarias {} litros de tinta'.format(area, tinta))