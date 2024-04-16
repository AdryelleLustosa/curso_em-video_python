# Sorteio nome de  4 alunos e deixe em ordem aleatoria de apresentação  
import random

Aluno1 = input('Qual o seu nome? ')
Aluno2 = input('Qual o seu nome? ')
Aluno3 = input('Qual o seu nome? ')
Aluno4 = input('Qual o seu nome? ')

alunos = [Aluno1, Aluno2, Aluno3, Aluno4]

print ('Os alunos são: {}' .format(alunos))

escolhido = random.shuffle(alunos)

print ('A ordem de apresentação fica: {}' .format(alunos))
