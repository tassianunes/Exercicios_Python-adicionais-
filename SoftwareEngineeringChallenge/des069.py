contIdade = contH = contF = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        contIdade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Difite o sexo: [M/F] ')).strip().upper()
    if sexo in 'M':
        contH += 1
    if sexo in 'F':
        if idade < 20:
            contF += 1
    print('-'*20)
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar: [S/N] ')).strip().upper()
    if pergunta == 'N':
        break
print('='*5,end='')
print('FIM DO PROGRAMA', end='')
print('='*5)
print('Total de pessoas com mais de 18 anos: {}'.format(contIdade))
print('Ao todo temos {} homens cadastrados.'.format(contH))
print('E temos {} mulheres com menos de 20 anos.'.format(contF))