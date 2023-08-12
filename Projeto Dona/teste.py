import sys
sys.path.append('Pergunta_fala')
from jogo import conta
from Pergunta_fala import fala
import speech_recognition as sr


def linha():
    print('------------------------------')

def opcao(x, y): # x = numero / y = tema
    print(f'[{x}]: {y}')

def espaco():
    print('')

def roda():
    linha()
    print('|       MENU PRINCIPAL       |')
    linha()
    espaco()
    opcao('1', 'JOGO DO CALCULO')
    opcao('2', 'EXIT / SAIR')

    fala()
    print("Fale a resposta: ")
    rec = sr.Recognizer()

    with sr.Microphone(device_index=0) as mic:
        rec.adjust_for_ambient_noise(mic)
        audio = rec.listen(mic)
        frase = rec.recognize_google(audio, language="pt-BR")
        string = frase
        numeros = []
        for caractere in string:
            if caractere.isdigit():
                numeros.append(caractere)

        numero = "".join(numeros)
        print(numero)
    
    numero = str(numero)
    if numero == '1':
        linha()
        print('|    JOGO DE CALCULOS    |')
        linha()
        conta()
        roda()
    if numero == '2':
        print('FIM')
roda()