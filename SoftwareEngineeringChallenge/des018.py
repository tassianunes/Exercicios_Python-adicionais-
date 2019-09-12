from math import sin, cos, tan, radians
a = float(input('Digite o valor do angulo: '))
b = radians(a)
print('O ângulo {}, possui o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(a, sin(b), cos(b), tan(b)))