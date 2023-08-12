import speech_recognition as sr
import random
import time

contador = 0

def conta():
    global contador
    rec = sr.Recognizer()

    with sr.Microphone(device_index=0) as mic:
        n1 = random.randint(0,30)
        n2 = random.randint(0,30)
        soma = n1 + n2
        print(f'{n1} + {n2}?')
        rec.adjust_for_ambient_noise(mic)
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('')
        print("Responda em voz alta")
        audio = rec.listen(mic)
        frase = rec.recognize_google(audio, language="pt-BR")
        string = frase
        numero = ""
        for caractere in string:
            if caractere.isdigit():
                numero += caractere
            else:
                break
        print(numero)
        soma = str(soma)
        if numero == soma:
            print("Acertou")
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            contador += 1
            conta()
        elif numero == 0:
            print('')
        else:
            print(f"ERROU: a resposta certa -> {soma} / a sua resposta foi {numero}")
            print(f'Voce acertou {contador} vezes')
