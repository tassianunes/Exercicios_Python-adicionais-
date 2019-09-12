from datetime import date
atual = date.today().year
print('=-'*25)
print('\033[32mBEM VINDO A CONSULTA DE ALISTAMENTO MILITAR\033[m')
print('=-'*25)
while True:
    nome = str(input('Digite seu nome: '))
    nascimento = int(input('Ano de nascimento: '))
    idade = atual - nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
    if idade < 18:
        print('Ainda faltam {} anos para você se alistar'.format(18 - idade))
    elif idade == 18:
        print('Já está na hora de se alistar! Procure o comando mais próximo de sua casa.')
    else:
        print('Já passaram {} anos do seu alistamento.'.format(idade - 18))
    print('-'*20)
    pergunta = str(input('Deseja continuar: [S/N]')).strip().upper()
    print('-'*25)
    if pergunta in 'N':
        break
print('Obrigado por usar nosso serviço!')