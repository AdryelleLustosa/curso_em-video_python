# Ler o ano de nascimento de um atleta, e ver em qual categoria ele ficou.
# Até 9 anos, mirin. 14 anos: Infantil. 19 anos: Junior. 20 anos: Senior. Acima: Master

from datetime import datetime

print('---------------------------------------------------')
print('--------Confederação Nacional de Natação-----------')
print('---------------------------------------------------')

nome = str(input("Digite seu nome: "))
ano_nascimento = int(input('Digite o ano que nasceu: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if (idade > 0 and idade <= 9):
    print('Bem vindo {}! Por ter {} anos, sua categoria é Mirin'.format(nome, idade))
elif (idade > 9 and idade <=14):
    print('Bem vindo {}! Por ter {} anos, sua categoria é Infantil'.format(nome, idade))
elif (idade > 14 and idade <= 19):
    print('Bem vindo {}! Por ter {} anos, sua categoria é Junior'.format(nome, idade))
elif (idade > 19 and idade <= 20):
    print('Bem vindo {}! Por ter {} anos, sua categoria é Senior'.format(nome, idade))
elif (idade > 20 and idade <= 120):
    print('Bem vindo {}! Por ter {} anos, sua categoria é Master'.format(nome, idade))
else:
    print('Foi digitado o ano de nascimento incorretamente. Por favor, digite novamente')
