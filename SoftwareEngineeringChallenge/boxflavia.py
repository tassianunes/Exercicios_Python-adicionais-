print('-=' * 15)
print('WELCOME TO BEHAVIOR TASK')
print('-=' * 15)

##### PRIMEIRA ETAPA: HABITUAÇÃO ##### -
habituado = str(input("O animal está habituado? n = não, s= sim\n"))
if habituado == "s":
    print("O animal seguirá o teste para a segunda etapa.")

    ###### SEGUNDA ETAPA: DISTÂNCIA DO ANIMAL ##########

    distancia = int(input("Digite a distância do animal:\n"))
    if (distancia <= 30):
        print("Foi liberado 0,5 ml de rec!")
        print('O animal passou para a terceira fase.')

        ##### TERCEIRA ETAPA: TOQUE NA BARRA #########

        barra = int(input("Digite a quantidade de vezes em que o animal tocou na barra:\n"))
        if barra >= 20:
            print('animal passou para quarta fase')
            ###### QUARTA ETAPA: SOM PI E BARRA ESQUERDA #######
            som1 = str(input("Digite o som emitido:\n"))
            barrab = str(input("Digite a barra apertada:\n"))
            if som1 == "pi" and barrab == "esquerda":
                print("Parabéns, o animal passou para a quinta fase!")

                ########## QUARTA ETAPA: SOM2 E BARRA DIREITA #########
                som2 = str(input("Digite o som emitido:\n"))
                barraa = str(input("Digite a barra apertada:\n"))
                if som2 == "fi" and barraa == "direita":
                    print("Tudo certo! O animal passou para a próxima etapa.")
                    duraçao = int(input("Quanto tempo (em minutos) durou esse experimento?\n"))
                    repetiçao = int(input("Quantas vezes o experimento foi repetido? \n"))
                    if duraçao >= 30 and repetiçao >= 50:
                        print("Parabéns, o experimento seguirá para a próxima fase!")
                    else:
                        print("Tempo/repetição insuficiente para a continuar experimento.")
                else:
                    print("Algo deu errado. O som e a barra não correspondem, recompensa não foi liberada.")
            else:
                print("Ops. O som emitido e a barra não correspondem. Recompensa não liberada.")
        else:
            print('Recompensa não liberada. O animal precisa treinar mais.')
    else:
        print("Distância insuficiente para liberar REC")
else:
    print("Por favor, habitue o animal!")