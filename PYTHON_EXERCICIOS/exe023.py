# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

numero = str(input('Digite um número de 0 a 9999: '))
print(numero)
numerodividido = str(numero.split())
numerodividido.strip()
#print("Unidade: {} Dezena: {} Centena: {} Milhar {}".format(numerodividido[3], numerodividido[2], numerodividido[1], numerodividido[0]))
print('Unidade: ', numerodividido[5])
print('Dezena: ', numerodividido[4])
print('Centena: ', numerodividido[3])
print('Milhar: ', numerodividido[2])