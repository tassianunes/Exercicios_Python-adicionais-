p = float(input('qual é o preço do produto: R$ '))
d = int(input('Qual o desconto: '))
print('Este produto esta com {}% de desconto, ele custava R${:.2f} e agora você levará por R${:.2f}'.format(d, p, p-((p*d)/100)))