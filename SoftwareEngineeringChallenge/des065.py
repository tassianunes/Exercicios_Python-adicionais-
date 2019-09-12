resp = 'S'
cont = 0
soma = 0
while resp in 'S':
    num = int(input('Digite um numero: '))
    resp = str(input('Quer continuar: [S/N] ')).strip().upper()
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Você digitou {} números e a média foi {:.2f}'.format(cont, soma/cont))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))