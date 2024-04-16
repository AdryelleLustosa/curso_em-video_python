# Um programa que leia dois numeros inteiros e compares na tela

numero1= int(input("Digite o primeiro valor: "))
numero2= int(input("Digite o segundo valor: "))
print('Você digitou os numeros {} e {}'.format(numero1, numero2))

if(numero1 > numero2):
    print('O primeiro valor é maior que o segundo')
elif(numero1<numero2):
    print('O segundo valor é maior que o primeiro')
else:
    print('Não eixste valor maior, ambos são iguais')