n = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaços: {}'.format(n.isspace()))
print('É um número: {}'.format(n.isnumeric()))
print('É alfabético: {}'.format(n.isalpha()))
print('É alfanumérico: {}'.format(n.isalnum()))
print('Está em maiusculo: {}'.format(n.isupper()))
print('Está em minusculo: {}'.format(n.islower()))