from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade < 18:
    print('Ainda faltam {} anos para você se alistar'.format(18 - idade))
elif idade == 18:
    print('Já está na hora de se alistar! Procure o comando mais próximo de sua casa.')
else:
    print('Já passaram {} anos do seu alistamento.'.format(idade - 18))