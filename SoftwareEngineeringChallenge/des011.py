# Aula 07 - Operadores matemáticos
l = float(input('Qual é a largura da parede: '))
a = float(input('Qual é a altura da parede: '))
area = (l * a)
t = area / 2
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.2f}m2.'.format(l, a, area))
print('Para pintar essa parede, você precisará de {:.1f} litros de tinta.'.format(t))
