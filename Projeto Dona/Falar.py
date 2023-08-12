import gtts
from playsound import playsound
import random

def comprimento():
    try:
        sorteio_fala = random.randint(2,7)


        if sorteio_fala < 0:
            print('ERRO')
        elif sorteio_fala == 2:
            with open('frase2.txt', 'r') as arquivo2:
                for linha2 in arquivo2:
                    frase2 = gtts.gTTS(linha2, lang='pt-BR')
                    frase2.save('frase2.mp3')
                    playsound('frase2.mp3')
        elif sorteio_fala == 3:
            with open('frase3.txt', 'r') as arquivo3:
                for linha3 in arquivo3:
                    frase3 = gtts.gTTS(linha3, lang='pt-BR')
                    frase3.save('frase3.mp3')
                    playsound('frase3.mp3')

        elif sorteio_fala == 4:
            with open('frase4.txt', 'r') as arquivo4:
                for linha4 in arquivo4:
                    frase4 = gtts.gTTS(linha4, lang='pt-BR')
                    frase4.save('frase4.mp3')
                    playsound('frase4.mp3')

        elif sorteio_fala == 5:
            with open('frase5.txt', 'r') as arquivo5:
                for linha5 in arquivo5:
                    frase5 = gtts.gTTS(linha5, lang='pt-BR')
                    frase5.save('frase5.mp3')
                    playsound('frase5.mp3')

        elif sorteio_fala == 6:
            with open('frase6.txt', 'r') as arquivo6:
                for linha6 in arquivo6:
                    frase6 = gtts.gTTS(linha6, lang='pt-BR')
                    frase6.save('frase6.mp3')
                    playsound('frase6.mp3')

        elif sorteio_fala == 7:
            with open('frase7.txt', 'r') as arquivo7:
                for linha7 in arquivo7:
                    frase7 = gtts.gTTS(linha7, lang='pt-BR')
                    frase7.save('frase7.mp3')
                    playsound('frase7.mp3')
    except:
        comprimento()