while True:
    print('-'*33)
    numeroInp = int(input('Quer ver a tabuada de qual valor: '))
    print('-'*33)
    if numeroInp < 0:
        break
    for c in range(1,11):
        print('{} x {} = {}'.format(numeroInp, c, numeroInp*c))
print('PROGRAMA TABUADA ENCERRADO! VOLTE SEMPRE!')