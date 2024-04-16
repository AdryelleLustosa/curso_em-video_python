aleatorio = input('Digite algo: ')
print('O tipo primitivo desse valor é :', type(aleatorio)) #Tipo
print('So tem espaços? ', aleatorio.isspace()) #Se so tem espaçoes
print('É um numerico? ', aleatorio.isnumeric()) # Se é numerico (mesmo se for um numero tipo str, vi dizer se é numero)
print('É alfabetico? ', aleatorio.isalpha()) # Se é letra (str)
print('É Alfanumerico? ', aleatorio.isalnum()) # se tem numeros e letras
print('Está em maisuclo? ', aleatorio.isupper()) # se está em maiusculas
print('Está em minusculo? ', aleatorio.islower()) # Se está em minusculas

