# Faça um programa que leia o ano de nascimento e informe, de acordo com a idade se: 
# Ele pode se alistar, se é hora de se alistar, ou se ja passou da hora.

from datetime import datetime

ano_atual = datetime.now().year


nome = str(input('Qual o seu nome? '))
ano_nascimento = int(input('Em qual ano você nasceu: '))
ano_atual = datetime.now().year
idade = (ano_atual - ano_nascimento)
print(idade)

if(ano_nascimento < 1950 or ano_nascimento > ano_atual or " "):
    print('Data invalida, digite novamente')
else:
    if(idade < 17):
        diferença_idade = 17 - idade
        print('{}, Com {} anos você não pode se alistar no exercito. Ainda faltam: {} anos'.format(nome, idade, diferença_idade))
    elif(idade > 22):
         diferença_idade = idade - 22
         print('{}, Com {} anos você não pode se alistar no exercito. Ja passou: {} anos desde o limite maximo'.format(nome,idade, diferença_idade)) 
    else:
        print('{}, Com {} você está pronto para se alistar no exercito!'.format(nome,idade))


