print('-='*10)
print('BAHAVIOUR BOX')
print('-='*10,'\n')
print('''Suas opções:
[ 0 ] Não habituado
[ 1 ] Habituação\n''')
habituacao = int(input('O animal está habituado: '))

if habituacao:
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
        if barra >= 20:
            print('O animal passou para a etapa 3!')
            print('\nETAPA 3: Discriminação do som e barra')
            print('Suas opções de som e barra: ')
            print('[ 1 ] Som 1: Phi')
            print('[ 2 ] Som 2: Trill')
            print('[ 3 ] Barra direita')
            print('[ 4 ] Barra esquerda')
            som = int(input('Digite o som reproduzido: '))
            direcaoBarra = int(input('Qual barra foi tocada: '))
            if som == 1 and direcaoBarra == 4:
                print('Foi liberado 0,5 ml de recompensa!')
                trials = int(input('\nNumero de trials: '))
                duracao = int(input('\nTempo duração experimento: '))
                if trials >= 50 and duracao <= 30:
                    print('O experimento seguirá para proxima fase!')
                else:
                    print('Repitir o teste até atingir o tempo ideal!')
            elif som == 2 and direcaoBarra == 3:
                print('Foi liberado 0,5 ml de recompensa!')
                trials = int(input('Numero de trials: '))
                duracao = int(input('Tempo duração experimento: '))
                if trials >= 50 and duracao <= 30:
                    print('\nO experimento seguirá para proxima fase!')
                else:
                    print('Repitir o teste até atingir o tempo ideal!')
            else:
                print('A recompensa não foi liberada!')
        else:
            print('O animal deverá ficar nessa etapa até atingir o objetivo!')
    else:
        print('O animal devera ficar na ETAPA 1 até atingir o objetivo!')
else:
    print('Antes de realizar o experimento o animal deverá ser habituado!\n')