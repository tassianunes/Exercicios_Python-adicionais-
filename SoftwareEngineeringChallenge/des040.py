nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua média é {}'.format(media))
if media < 5.0:
    print('\033[31mREPROVADO!')
elif media >= 5 and media < 7:
    print('\033[34mRECUPERAÇÃO!')
else:
    print('\033[32mAPROVADO!')