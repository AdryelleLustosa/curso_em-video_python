# Programa que leia o peso de cinco pessoas e mostre o peso maior e o menor

peso_maior = 0
peso_menor = 100

for contador in range(0,5):
    peso = float(input("Digite seu peso: "))
    
    if peso > peso_maior:
        peso_maior = peso
        

    if(peso < peso_menor):
        peso_menor = peso
       
       
    
      
    
print("Peso maior é: {} ".format(peso_maior))
print("Peso menor é: {} ".format(peso_menor))

