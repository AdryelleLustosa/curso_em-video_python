# Um programa que leia uma frase e mostre:
# Quantas vezes aparece o A
# Em que posição ele aparece a primeira vez
# Em que posição ele aparece a ultima vez

frase = str(input('Escreva uma frase: ')).lower()
print("A letra A aparece: {} vezes".format(frase.count('a')))
print("A posição da primeira letra a está: : {}".format(frase.find('a')))
print("A posição da primeira letra a está: : {}".format(frase.rfind('a')))




