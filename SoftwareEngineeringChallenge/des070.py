print('='*20)
print('AI.WA STORE')
print('='*20)
soma = caro = barato = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    soma += preco
    if preco > 1000:
        caro += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-'*5,end = ' ')
print('FIM DO PROGRAMA',end = ' ')
print('-'*5)
print('O total da compra foi {}'.format(soma))
print('Temos {} proutos custando mais de 1000 reais.'.format(caro))

