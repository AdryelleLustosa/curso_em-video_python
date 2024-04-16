# Escreva um prgrama que faça o computador pensar em um número inteiro entre 0 e 5,= e peça para o usuario tentar descobrir 

computador = 3
numero_escolhido = int(input('Escolha um número de 0 a 5: '))

if (numero_escolhido == computador):
    print('Você venceu!!!')
else:
    print('Você perdeu :(')