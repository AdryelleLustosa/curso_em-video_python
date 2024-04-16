# Programa que calcule aumento de salario
# Se o salario for maior que 1250,00 caulcule aumento de 10%
# menores, o aumento é 15%

salario = float(input('Descreva o valor do seu salario: '))

if (salario > 1250):
    aumento = (salario * (10/100))+salario
    print('Seu salario vai de {} reais para {} reais'.format(salario, aumento))
else:
    aumento = ((salario*(15/100)+ salario))
    print('Seu salario vai de {} reais para {} reais'.format(salario, aumento))
