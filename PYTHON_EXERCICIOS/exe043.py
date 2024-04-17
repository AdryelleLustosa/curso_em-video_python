# Calculadora IMC


nome = str(input("Digite seu nome: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = (peso/(altura*altura))

print('---------------------------------------------------')
print('-------------***Calculadora IMC***-----------------')
print('---------------------------------------------------')

print('Menor que 18.5: Abaixo do peso --------------------')
print('Entre 18.5 e 25: Peso ideal -----------------------')
print('Entre 25 e 30: Sobrepeso --------------------------')
print('Entre 30 e 40: Obesidade --------------------------')
print('Acima de 40: Obesidade Morbita---------------------')



if (IMC > 0 and IMC <= 18.5):
    print('Olá {}, seu IMC está {:.2f} e você está abaixo do peso. Sugerimos procurar um nutricionista!'.format(nome, IMC))
elif(IMC > 18.5 and IMC <25): 
    print('Olá {}, seu IMC está {:.2f} e você está com seu peso ideal. Continue assim! '.format(nome, IMC))
elif(IMC >= 25 and IMC <30):
    print('Olá {}, seu IMC está {:.2f} e você está com sobrepeso. Sugerimos procurar um nutricionista! '.format(nome, IMC))
elif (IMC >=30 and IMC < 40):
    print('Olá {}, seu IMC está {:.2f} e você está com obesidade. Sugerimos procurar um nutricionista! '.format(nome, IMC))
elif(IMC >= 40): 
    print('Olá {}, seu IMC está {:.2f} e você está com obesidade morbita. Sugerimos procurar um nutricionista! '.format(nome, IMC))


