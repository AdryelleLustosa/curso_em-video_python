# Programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras tem ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Escreva seu nome completo: '))
print (nome.upper())
print (nome.lower())
print (len(nome.strip()))
nomedividido = nome.split()
print (len(nomedividido[1]))