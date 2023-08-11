from jogo import conta

def linha():
    print('------------------------------')

def opcao(x, y): # x = numero / y = tema
    print(f'[{x}]: {y}')

def espaco():
    print('')

def roda():
    linha()
    print('        MENU PRINCIPAL        ')
    linha()
    espaco()
    opcao('1', 'JOGO DO CALCULO')

    perg = int(input ("Insira a resposta: "))
    if perg == 1:
        conta()
        roda()
roda()