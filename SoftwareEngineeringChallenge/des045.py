from time import sleep
from random import randint
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Qual sua jogada? '))
computador = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*15)
print('\033[32mComputador jogou {}'.format(itens[computador]))
print('\033[34mJogador jogou {}\033[m'.format(itens[jogador]))
print('-='*15)
if jogador != computador:
    if jogador == 0 and computador == 1:
        print('Você perdeu!')
    elif jogador ==0 and computador == 2:
        print('Você VENCEU!')
    elif jogador == 1 and computador == 0:
        print('você VENCEU!')
    elif jogador == 1 and computador == 2:
        print('você PERDEU! ')
    elif jogador == 2 and computador == 0:
        print('você perdeu!')
    else:
        print('você VENCEU!')
else:
    print('EMPATE')