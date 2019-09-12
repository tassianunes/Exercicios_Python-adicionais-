peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / (altura**2)
print('Seu IMC é de {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso!')
elif IMC >= 18.5 and IMC < 25:
    print('Você está no peso ideal!')
elif IMC >=25 and IMC < 30:
    print('Você está com sobrepeso!')
elif IMC >= 30 and IMC <40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')