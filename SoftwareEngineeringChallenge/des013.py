nome = str(input('Qual é o seu nome: '))
s = float(input('Qual é o seu salário: R$ '))
a = int(input('Qual é a porcentagem de aumento: '))
print('Olá {},\nSeu salário era de {:.2f}.\n Parabéns você recebeu um aumento de {}%.\n Seu novo salário é {:.2f}.'.format(nome, s, a, s +((a*s)/100)))