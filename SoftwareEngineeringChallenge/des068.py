from random import randint
computador = randint(0,10)
cont = 0
while True:
    print('=-'*15)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-'*15)
    jogador = int(input('Diga um valor: ' ))
    escolha = str(input('PAR ou IMPAR: [P/I] ')).strip().upper()
    soma = jogador + computador
    if soma%2 == 0:
        if escolha == 'P':
            print('Você jogou {} e o computador {}. Total de {} DEU {}'.format(jogador, computador, soma,'PAR'))
            print('Você venceu vamos jogar novamente...')
            cont +=1
        elif escolha =='I':
            print('Você jogou {} e o computador {}. Total de {} DEU {}'.format(jogador, computador, soma, 'PAR'))
            print('Voce \033[34mperdeu\033[m.')
            break
    else:
        if escolha == 'P':
            print('Você jogou {} e o computador {}. Total de {} DEU {}'.format(jogador, computador, soma, 'IMPAR'))
            print('Voce \033[34mPERDEU\033[m.')
            break
        elif escolha == 'I':
            print('Você jogou {} e o computador {}. Total de {} DEU {}'.format(jogador, computador, soma, 'ÍMPAR'))
            print('Você venceu vamos jogar novamente...')
            cont+=1
print('\033[33mGAME OVER! Você venceu {} vezes'.format(cont))
