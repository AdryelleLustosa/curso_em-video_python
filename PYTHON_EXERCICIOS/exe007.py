# Programa para ler notas de aluno

nome = input('Qual o seu nome? ')
nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media_notas = float((nota_1+nota_2)/2)

print('Então {}, a sua média foi: {}'.format(nome,media_notas))