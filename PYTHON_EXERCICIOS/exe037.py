# Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a conversão 
# 1 Para binario
# 2 para octal
# 3 para hexadecimal

numero = int(input('Digite o numero: '))

print('---------------------------------------------------------------------------')

base_conversão = int(input("""Escolha uma opção para sua base de Conversão:
[1] Binario
[2] Octal
[3] Hexadecimal """))

if (base_conversão == 1):
    numero_convertido = bin(numero)
    nome_base = 'Binario'
    print('O numero {} convertido em {} é igual a {}'.format(numero, nome_base, numero_convertido))

elif (base_conversão == 2):
    numero_convertido = oct(numero)
    nome_base = 'Octal'
    print('O numero {} convertido em {} é igual a {}'.format(numero, nome_base, numero_convertido))

elif (base_conversão == 3):
    numero_convertido = hex(numero)
    nome_base = 'Hexadecimal'
    print('O numero {} convertido em {} é igual a {}'.format(numero, nome_base, numero_convertido))
else:
    print('Digite uma opção valida')

