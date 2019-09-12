print('-='*20)
print('AUTOMATIC BEHAVIOR')
print('-='*20,'\n')
print('''Suas opções:
[ 0 ] Não habituado
[ 1 ] Habituado\n''')
habituacao = int(input('O animal está habituado: '))
if habituacao == 0:
    print('Antes de realizar o experimento, o animal deverá ser habituado!\n')

else:
    print('\nAlguns parâmetros serão avaliados na seguinte ordem!')
    print('ETAPA 1: Aproximação da barra')
    print('ETAPA 2: Tocar na barra')
    print('ETAPA: Discriminar o som')
    print('\nETAPA 1: APROXIMAÇÃO')
    distancia = int(input('Distância do animal até a barra: '))
    if distancia <= 30:
        print('Foi liberado 0,5 ml de recompensa!')
        print('O animal passou para etapa 2')
        print('\nETAPA 2: TOCAR NA BARRA')
        barra = int(input('Quantas vezes tocou na barra: '))
        if barra >=20:
            print('O animal passou para a etapa 3!')
            print('\nETAPA 3: Discriminação do som')
            print('Suas opções de som: ')
            print('[ 1 ] Som 1: Phi')
            print('[ 2 ] Som 2: Trill')
            print('[ 3 ] Barra direita')
            print('[ 4 ] Barra esquerda')
            som = int(input('Digite o som reproduzido: '))
            direcaoBarra = int(input('Qual barra foi tocada: '))
            if som == 1 and direcaoBarra == 4:
                print('Foi liberado 0,5 ml de recompensa!')
            elif som ==2 and direcaoBarra ==3:
                print('Foi liberado 0,5 ml de recompensa!')
            else:
                print('A recompensa não foi liberada!')
        else:
            print('O animal deverá ficar nessa etapa até atingir o objetivo!')
    else:
        print('O animal devera ficar na ETAPA 1 até atingir o objetivo!')