from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Você tem {} anos'.format(idade))
if idade <= 9:
    print('categoria MIRIM!')
elif 9 < idade <= 14:
    print('categoria INFANTIL!')
elif 14 < idade <= 19:
    print('categoria JUNIOR!')
elif idade == 20:
    print('categoria SÊNIOR!')
else:
    print('categoria MASTER!')