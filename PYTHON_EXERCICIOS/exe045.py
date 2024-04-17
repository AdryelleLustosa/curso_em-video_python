# Crie um Programa que faça o computador jogar Pedra, Papel e tesoura com você

import random


escolhido = ["PEDRA", "PAPEL", "TESOURA"]
minha_escolha = str(input("""Escolha su opção: PEDRA ou PAPEL ou TESOURA \n"""))
escolha_computador = random.choice(escolhido)

if (minha_escolha == "PEDRA"):
    if (escolha_computador == "PEDRA"):
        print("""PEDRA X PEDRA
              Empatou! Tente novamente""")
    if (escolha_computador == "TESOURA"):
        print("""PEDRA X TESOURA
              Você ganhou!!!!""")
    if (escolha_computador == "PAPEL"):
        print("""PEDRA X PAPEL
              Você perdeu!!!!""")
        
elif (minha_escolha == "PAPEL"):
    if (escolha_computador == "PEDRA"):
        print("""PAPEL X PEDRA
              Você ganhou!!!!""")
    if (escolha_computador == "TESOURA"):
        print("""PAPEL X TESOURA
              Você perdeu!!!!""")
    if (escolha_computador == "PAPEL"):
        print("""PAPEL X PAPEL
              Empatou! Tente novamente""")
        
elif (minha_escolha == "TESOURA"):
    if (escolha_computador == "PEDRA"):
        print("""TESOURA X PEDRA
              Você perdeu!!!!""")
    if (escolha_computador == "TESOURA"):
        print("""TESOURA X TESOURA
              Empatou! Tente novamente""")
    if (escolha_computador == "PAPEL"):
        print("""TESOURA X PAPEL
              Você ganhou!!!!""")
        
else:
    print('Opção invalida, tente novamente')








