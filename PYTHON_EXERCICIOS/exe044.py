# Um programa que calcule o valor a ser pago por um produto
#Considerando seu preço normal e condição de pagamento

preco_produto = float(input('Digite o valor do produto: '))
forma_pagamento = int(input('''Escolha a forma de pagamento:
    *** [1] À vista: Dinheiro ou Cheque ***
    *** [2] À vista: No cartão ***
    *** [3] Em até 2x no cartão ***
    *** [4] 3x ou mais no cartão ***  '''))


if (forma_pagamento == 1):
    preco_produto_final = preco_produto-(preco_produto*(10/100))
    print("O valor do seu produto é {:.2f} reais, você ganhou um desconto de 10%!!! O valor final a pagar é {:.2f} reais ".format(preco_produto, preco_produto_final))
elif(forma_pagamento == 2):
    preco_produto_final = preco_produto-(preco_produto*(5/100))
    print("O valor do seu produto é {:.2f} reais, você ganhou um desconto de 5%!!! O valor final a pagar é {:.2f} reais ".format(preco_produto, preco_produto_final))
elif(forma_pagamento == 3):
    print("O valor final da sua compra foi: {:.2f} reais".format(preco_produto))
elif(forma_pagamento == 4):
    preco_produto_final = preco_produto+(preco_produto*(20/100))
    print("O valor do seu produto é {:.2f} reais, por parcelar em 3 vezes ou mais,o valor final a pagar é {:.2f} reais ".format(preco_produto, preco_produto_final))
else:
    print('Forma de pagamento invalida, escolha novamente')