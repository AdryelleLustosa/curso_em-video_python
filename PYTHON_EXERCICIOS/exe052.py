# Ler número inteiro, e dizer se ele é ou não número primo

numero = int(input('Digite um valor: '))
soma = 0

for contador in range (1, numero+1):
   
    if ((numero%contador) ==0 ): 
        soma+=1

if (soma == 2):
    print('{} É um número primo'.format(numero))
else:
    print('{} Não é um número primo'.format(numero))
    
