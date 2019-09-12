num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[ 1 ] coverter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:])) #[2:] é um fatiamento do caracter para retirar o codigo de binario
elif opcao == 2:
    print('{} convertido em OCTAL é {}'.format(num, oct(num)[2:]))
else:
    print('{} convertido em HEXADECIMAL é {}'.format(num, hex(num)[2:]))