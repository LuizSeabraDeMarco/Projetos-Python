import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone(device_index=0) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Fale alguma coisa")
    audio = rec.listen(mic)
    frase = rec.recognize_google(audio, language="pt-BR")
    print(frase)