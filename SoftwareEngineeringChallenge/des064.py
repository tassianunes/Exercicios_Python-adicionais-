numero = 0
cont = 0
contInputs = 0
while numero != 999:
    numero = int(input('Digite um numero: [999 para parar]: '))
    if numero != 999:
        cont += numero
        contInputs += 1
    else:
        print('Finalizando...')
print('Você digitou {} numeros e a soma entre eles foi {}'.format(contInputs, cont))
