soma = 0
cont = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        soma += c
        cont += 1
print('O total de impares multiplos de 3 foram {} e sua soma é {}'.format(cont, soma))