# Programa que leia seis numeros inteiros. mostre a soma dos numeros pares


soma = 0
for contador in range(0,6):
    numero = int(input("Digite um valor inteiro: "))
    if ((numero % 2)==0):
        soma+=numero
print(soma)

