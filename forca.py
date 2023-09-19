import unicodedata

def coração(x, y=0):
    coracao_lista = []
    coracao = unicodedata.lookup('HEAVY BLACK HEART')
    while True:
        if y < x:
            coracao_lista.append(coracao)
            y = y + 1
        else:
            print('VIDA:  ' + ' '.join(coracao_lista))
            break

def forca():
    palavra_escolhida = str(input('Escolha uma palavra: '))
    palavra_escolhida = palavra_escolhida.lower()

    if not palavra_escolhida.isdigit():
        def espaco(x=0):
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

        def jogo(vida):
            while vida > 0:
                coração(vida)
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
                            print('Letras que não são: ')
                            print(letra_errada)
                            # Mostra a palavra com as letras adivinhadas na ordem correta
                            print(' '.join(palavra_mostrada))
                            linha()
                            if '_' not in palavra_mostrada:
                                print('A palavra é ' + palavra_escolhida)
                                return
                        else:
                            linha()
                            if letra in letra_encontrada or letra in letra_errada:
                                print('Letra já inserida')
                            else:
                                print('Esta letra não está na palavra')
                                vida -= 1
                                coração(vida)
                                letra_errada.append(letra)
                                if vida == 0:
                                    print('Acabaram suas vidas')
                                    return
                                print('NÃO TEM:  ' + ' '.join(letra_errada))
                            linha()
                    else:
                        print('Digite apenas uma letra por vez')
                else:
                    print('DIGITE APENAS LETRAS')
            print('Você perdeu! A palavra era ' + palavra_escolhida)

        return jogo

def dificuldade():
    print('[1] Facil(10 vidas)')
    print('[2] Medio(7 vidas)')
    print('[3] Dificil(5 vidas)')
    dificuldade_input = int(input('Digite a dificuldade: '))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')
    if 0 < dificuldade_input < 4:
        if dificuldade_input == 1:
            jogo_facil = forca()
            jogo_facil(10)
        elif dificuldade_input == 2:
            jogo_medio = forca()
            jogo_medio(7)
        elif dificuldade_input == 3:
            jogo_dificil = forca()
            jogo_dificil(5)
    else:
        dificuldade()

dificuldade()
