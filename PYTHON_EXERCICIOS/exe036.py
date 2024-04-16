# Escrever um programa que simule um empréstimo bancario;
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario
# Se exceder o emprestimo será negado

valor_casa = int(input("Digite o valor da casa: "))
salario = int(input("Digite o valor do salario: "))
tempo_financiamento = int(input('Digite por quantos anos quer financiar: '))


prestação = valor_casa/(tempo_financiamento*12)

if prestação <= salario*(30/100):
    print('Seu empréstimo foi aceito! Você irá pagar a parcela de {} reais por {} anos'.format(prestação, tempo_financiamento))
else:
    print('Seu empréstimo foi negado! Sua renda é incompativel')

print('Agradecemos a preferencia')