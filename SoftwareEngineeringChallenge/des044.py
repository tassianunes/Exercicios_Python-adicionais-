print('\033[32m='*10, end='')
print('GAMER STORE',end='')
print('\033[32m=\033[m'*10)
valor = float(input('Valor do produto: '))
print('''Escolha qual forma de pagamento você irá efetuar:
[ 1 ] A vista: dinheiro/cheque
[ 2 ] A vista no cartão
[ 3 ] Parcelado em até 2x no cartão
[ 4 ] Parcelado em até 3x ou mais no cartão''')
opcao = int(input('Escolha sua opção: '))
if opcao == 1:
    preco1 = valor - ((valor*10)/100)
    print('Sua compra de {} vai custar {} você receu {}% de desconto!'.format(valor, preco1, 10))
elif opcao == 2:
    preco2 = valor - ((valor*5)/100)
    print('Sua compra de {} ai custar {}, você recebu {}% de desconto!'.format(valor, preco2,5))
elif opcao ==3:
    print('Sua compra vai ficar no valor de {}'.format(valor))
else:
    preco3 = valor + ((valor*20)/100)
    print('Sua compra de {} vai custar {}, foi acrescido {}% de juros. Que equivale a um aumento de {}.'.format(valor, preco3, 20, valor*20/100))