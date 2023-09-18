def forca():
    palavra_escolhida = str(input('Escolha uma palavra: '))
    palavra_escolhida = palavra_escolhida.lower()


    if not palavra_escolhida.isdigit():
        def espaco(x = 0):
            while True:
                if x < 100:
                    print(' ')
                    x = x + 1
                else:
                    break

        def linha():
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')

        espaco()

        # Cria uma lista com a palavra escolhida
        palavra = list(palavra_escolhida)

        # Cria uma lista de espaços vazios do mesmo tamanho da palavra escolhida
        palavra_mostrada = ['_' for _ in palavra_escolhida]

        letra_encontrada = []
        letra_errada = []
        def jogo():
            vida = int(10)
            while True:
                letra = str(input('Digite uma letra: '))
                letra = letra.lower()
                if not letra.isdigit():
                    numero_letra_resposta = len(letra)
                    if numero_letra_resposta == 1:
                        if letra in palavra:
                            linha()
                            # Substitui os espaços vazios pela letra adivinhada
                            for i in range(len(palavra)):
                                if palavra[i] == letra:
                                    palavra_mostrada[i] = letra
                            letra_encontrada.append(letra)
                            print( 'Letras que não são: ')
                            print(letra_errada)
                            # Mostra a palavra com as letras adivinhadas na ordem correta
                            print(' '.join(palavra_mostrada))
                            linha()
                            if '_' not in palavra_mostrada:
                                print('A palavra é '+ palavra_escolhida)
                                break
                            if len(palavra_escolhida) == len(letra_encontrada):
                                break
                        else:
                            linha()
                            if letra in letra_encontrada:
                                print('Letra já incerida')
                            else:
                                vida = vida - 1
                                print(vida)
                                print('Está letra não tem na palavra')
                                letra_errada.append(letra)
                                if int(vida) == 0:
                                    print('Acabou as suas vidas')
                                    break
                                print('NÃO TEM:  ' + ' '.join(letra_errada))
                            linha()
                else:
                    print('DIGITE APENAS LETRAS')
                    jogo()
                if len(letra_encontrada) == len(palavra_escolhida):
                    break
        jogo()
    else:
        print('DIGITE APENAS LETRAS')
        forca()


forca()