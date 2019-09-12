list = ('zero', 'um','dois', 'tres','quatro','cinco','seis', 'sete','oito','nove'
            'Dez','Onze','Doze', 'Treze','Catorze','quinze','dezesseis','dezessete',
           'dezoito','dezenove', 'vinte')
while True:
    numeroInp = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numeroInp <=20:
        break
    print('Tente novamente. ', end=' ')
print('Você digitou o número {}'.format(list[numeroInp]))