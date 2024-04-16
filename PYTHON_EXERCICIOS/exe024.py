#Crie um programa que leia o nome da sua cidade, e ele vai dizer se começa com a palavra santo: 

cidade = str(input('Escreva o nome da sua cidade: '))

cidadedividida = cidade.split()
print(cidadedividida[0] == 'Santo')

#print('Santo' in cidadedividida[0])