numero = int(input('Digite um numero \npara calcular seu Fatorial: '))
print('Calculando {}! = '.format(numero), end='')
cont = numero
fatorial = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ',end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))
