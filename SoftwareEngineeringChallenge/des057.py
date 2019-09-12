sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dado Inválido. por favor digite seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso.'.format(sexo))