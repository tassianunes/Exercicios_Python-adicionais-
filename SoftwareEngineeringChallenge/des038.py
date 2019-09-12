num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O primeiro valor é \033[32mMAIOR\033[m!')
elif num2 > num1:
    print('O segundo valor é \033[32mMAIOR\033[m!')
else:
    print('Não existe valor maior, os dois são iguais!')