import gtts
from playsound import playsound
import random
import os

sorteio_fala = random.randint(1,2)
sorteio_fala = 1
print(sorteio_fala)


if sorteio_fala < 0:
    print('ERRO')
elif sorteio_fala == 1:
    file = open("frase.txt", 'r')  
    with file as arquivo:
        for linha in arquivo:
            frase1 = gtts.gTTS(linha, lang='pt-BR')
            frase1.save('frase.mp3')
            playsound('frase.mp3')
elif sorteio_fala == 2:
    with open('frase2.txt', 'r') as arquivo2:
        for linha2 in arquivo2:
            frase2 = gtts.gTTS(linha2, lang='pt-BR')
            frase2.save('frase2.mp3')
            playsound('frase2.mp3')