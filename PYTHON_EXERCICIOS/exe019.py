# Sorteio nome de  4 alunos
import random

Aluno1 = input('Qual o seu nome? ')
Aluno2 = input('Qual o seu nome? ')
Aluno3 = input('Qual o seu nome? ')
Aluno4 = input('Qual o seu nome? ')

alunos = [Aluno1, Aluno2, Aluno3, Aluno4]

escolhido = random.choice(alunos)

print('O aluno sorteado foi: {}' .format(escolhido))

