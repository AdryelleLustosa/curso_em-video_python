# Programa que calcule a soma entre todos os números ímpares que são multiplos de três entre 1 e 500

soma = 0

for contador in range (0,500,3):
    if (contador % 3== 0):
        soma += contador
print("A soma de todos os números multiplos de 3 é: {}".format(soma))    

  