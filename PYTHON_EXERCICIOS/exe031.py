# Desenvolva um programa que pergunta a distancia em KM e calcula a passagem
# Ele cobra 0,50 em KM para viagens até 200KM e 0,45 para viagens mais longas

distancia = int(input('Qual a distancia da sua viagem? '))

if(distancia <= 200):
    valor = int(distancia * 0.50)
    print('O valor da sua passagem é: {} reais'.format(valor))
else:
    valor = int(distancia*0.45)
    print('O valor da sua passagem é: {} reais'.format(valor))

print('Obrigada por escolher nossa companhia')