# ler numero e dizer se é par ou impar

numero = int(input('Digite um número: '))
resto_numero = numero % 2

print('PAR') if resto_numero == 0 else print('impar')