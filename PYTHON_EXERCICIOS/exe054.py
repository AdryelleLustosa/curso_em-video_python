# Prgrama que leia o ano de nascimento de 6 pessoas, e diga se elas são maiores ou não

from datetime import datetime

maioridade = 0
menoridade = 0
ano_atual = datetime.now().year

for contador in range(0,6):
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    idade = ano_atual-ano_nascimento
    if(idade >= 18):
        maioridade+=1
        
    elif (idade >= 0 and idade <18):
        menoridade+=1
        
    else:
        print("Sua idade está incorreta")

print("{} pessoas tem maioridade".format(maioridade))
print("{} pessoas tem menoridade".format(menoridade))



