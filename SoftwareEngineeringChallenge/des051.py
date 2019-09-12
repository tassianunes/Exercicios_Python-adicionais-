primeiroTermo = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
termoFinal = primeiroTermo + ((10 -1)*razao)
for c in range (primeiroTermo, termoFinal+razao, razao):
    print('{}'.format(c),end=' -> ')
print('ACABOU')