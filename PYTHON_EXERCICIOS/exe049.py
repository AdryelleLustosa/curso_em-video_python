# Fazer uma tabuada
import time
numero = int(input('Digite um valor: '))

for contador in range (1,11):
    tabuada = numero * contador 
    print('{} x {} = {}'.format(numero, contador, tabuada))
    time.sleep(1)

