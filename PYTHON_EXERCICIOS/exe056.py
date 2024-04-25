# Programa que leia nome, idade, e sexo de 4 pessoas e no final mostre: 
# A media de idade, o nome do homem mais velho, e quantos muulheres tem mais de 21 anos

idadesoma = 0
idadehomem = 0
nomehomem = " "
idademulher = 0

for contador in range (1,5):
    
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = int(input("Qual o seu sexo: [1] Masculino [2] Feminino  "))
    idadesoma +=idade

    if sexo == 1:
        if idadehomem < idade:
            idadehomem = idade
            nomehomem = nome
    elif sexo == 2:
        if idade < 20:
            idademulher += 1 
    else:
        print("Sexo incorreto")



print("A média de idade do grupo é {:.1f} anos ".format(idadesoma/4))
print("O nome do Homem mais vleho é: {}".format(nomehomem))
print("Tem {} mulheres com idade abaixo dos 20 anos ".format(idademulher))
