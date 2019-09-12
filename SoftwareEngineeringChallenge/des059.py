from time import sleep
numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor:'))
escolha = 0
while escolha != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    escolha = int(input('>>>> Qual sua opção: '))
    if escolha == 1:
        print('A soma de {} e {} é {}'.format(numero1, numero2, numero1 + numero2))
    elif escolha == 2:
        print('A multiplicação entre {} e {} é {}'.format(numero1, numero2, numero1*numero2))
    elif escolha == 3:
        if numero1 > numero2:
            print('{} é maior que {}'.format(numero1, numero2))
        elif numero1 == numero2:
            print('{} é igual a {}'.format(numero1, numero2))
        else:
            print('{} é maior que {}'.format(numero2, numero1))
    elif escolha == 4:
        numero1 = int(input('Primeiro numero: '))
        numero2 = int(input('Segundo numero: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida tente novamente!')
    print('-='*15)
sleep(1)
print('Obrigado por testar o programa!')