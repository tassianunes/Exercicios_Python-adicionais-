cont = 0
soma = 0
while True:
    numeroInp = int(input('Digite um número: [999 para parar] '))
    if numeroInp == 999:
        break
    cont += 1
    soma += numeroInp
print('Você digitou {} números e a soma entre eles foi de {}.'.format(cont, soma))