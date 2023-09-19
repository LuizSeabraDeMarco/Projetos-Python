from jogo import conta
from Pergunta_fala import fala
import speech_recognition as sr

def linha():
    print('------------------------------')

def opcao(x, y):
    print(f'[{x}]: {y}')

def espaco():
    print('')

def roda():
    linha()
    print('|       MENU PRINCIPAL       |')
    linha()
    espaco()
    opcao('1', 'JOGO DO CÁLCULO')
    opcao('2', 'SAIR')

    fala()
    print("Fale a resposta: ")

    try:
        rec = sr.Recognizer()

        with sr.Microphone(device_index=0) as mic:
            rec.adjust_for_ambient_noise(mic)
            audio = rec.listen(mic)
            frase = rec.recognize_google(audio, language="pt-BR").lower()

        if 'um' in frase or '1' in frase:
            linha()
            print('|    JOGO DE CÁLCULOS    |')
            linha()
            conta()
            roda()
        elif 'dois' in frase or '2' in frase or 'sair' in frase:
            print('FIM')
        else:
            print('Opção não reconhecida')
            roda()
    except sr.UnknownValueError:
        print('Não foi possível entender a fala, tente novamente.')
        roda()
    except sr.RequestError:
        print('Erro na solicitação de reconhecimento de fala.')
        roda()
    except Exception as e:
        print(f'Erro inesperado: {str(e)}')
        roda()

roda()
