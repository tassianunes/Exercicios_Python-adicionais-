from random import randint
print('-'*20)
print('JOGADOR X COMPUTADOR')
print('-'*20)
print('Sou seu computador')
print('Acabei de pensar em um número entre 0 e 10!')
print('Será que você consegue advinhar qual foi?')
computador = randint(1,10)
palpite = int(input('Qual é seu palpite: '))
tentativas = 1
while palpite != computador:
    if palpite < computador:
        print('Mais..Tente mais uma vez!')
        palpite = int(input('Qual é seu palpite: '))
    else:
        print('Menos..Tente mais uma vez!')
        palpite= int(input('Qual é seu palpite: '))
    tentativas += 1
print('Acertou com {} tentativas Parabéns!'.format(tentativas))