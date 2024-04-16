# Crie um programa que mostra a media, e se o aluno reprovou ou passou

aluno = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

if (media > 0 and media < 5):
    print("{}, você ficou com a media de {:.1f}, sua situação é:  REPROVADO".format(aluno, media))
elif (media >= 7 and media <=10): 
    print("{}, você ficou com a media de {:.1f}, sua situação é APROVADO".format(aluno, media))
elif (media > 5 and media < 7):
    print("{}, você ficou com a media de {:.1f} sua situação é EM RECUPERAÇÂO".format(aluno, media))
else:
    print("Média Invalida")
