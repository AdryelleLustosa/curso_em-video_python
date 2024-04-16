# Programa que leia o cateto oposto e o cateto ajacente de um triangulo retangulo
#  calcule e moste e comprimento da hipotenusa

import math
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('O cateto oposto no valor de {} e o cateto adjacente no valor de {} a hipotenusa é: {}' .format(cateto_oposto, cateto_adjacente, math.ceil(hipotenusa)))

