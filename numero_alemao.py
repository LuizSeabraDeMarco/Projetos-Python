import tkinter as tk
from tkinter import messagebox
import random
from gtts import gTTS
import pygame
import threading

# Dicionários para mapear algarismos em palavras nos diferentes idiomas
numeros_idiomas = {
    'de': {
        0: "null", 1: "eins", 2: "zwei", 3: "drei", 4: "vier", 5: "fünf",
        6: "sechs", 7: "sieben", 8: "acht", 9: "neun", 10: "zehn",
        11: "elf", 12: "zwölf", 13: "dreizehn", 14: "vierzehn", 15: "fünfzehn",
        16: "sechzehn", 17: "siebzehn", 18: "achtzehn", 19: "neunzehn",
        20: "zwanzig", 30: "dreißig", 40: "vierzig", 50: "fünfzig",
        60: "sechzig", 70: "siebzig", 80: "achtzig", 90: "neunzig",
        100: "hundert", 1000: "tausend", 1000000: "million"
    },
    'it': {
        0: "zero", 1: "uno", 2: "due", 3: "tre", 4: "quattro", 5: "cinque",
        6: "sei", 7: "sette", 8: "otto", 9: "nove", 10: "dieci",
        11: "undici", 12: "dodici", 13: "tredici", 14: "quattordici", 15: "quindici",
        16: "sedici", 17: "diciassette", 18: "diciotto", 19: "diciannove",
        20: "venti", 30: "trenta", 40: "quaranta", 50: "cinquanta",
        60: "sessanta", 70: "settanta", 80: "ottanta", 90: "novanta",
        100: "cento", 1000: "mille", 1000000: "milione"
    },
    'fr': {
        0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq",
        6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix",
        11: "onze", 12: "douze", 13: "treize", 14: "quatorze", 15: "quinze",
        16: "seize", 17: "dix-sept", 18: "dix-huit", 19: "dix-neuf",
        20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante",
        60: "soixante", 70: "soixante-dix", 80: "quatre-vingts", 90: "quatre-vingt-dix",
        100: "cent", 1000: "mille", 1000000: "million"
    },
    'en': {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
        100: "hundred", 1000: "thousand", 1000000: "million"
    },
    'es': {
        0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco",
        6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez",
        11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince",
        16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve",
        20: "veinte", 30: "treinta", 40: "cuarenta", 50: "cincuenta",
        60: "sesenta", 70: "setenta", 80: "ochenta", 90: "noventa",
        100: "cien", 1000: "mil", 1000000: "millón"
    }
}

# Variáveis globais para controle do jogo
questoes_acertadas = 0
max_questoes_acertadas = 0
idioma_atual = ""
dificuldade_atual = ""
modo_jogo = "Numeros"
modo_escrita_ativo = False

# Funções para converter números em palavras nos diferentes idiomas
def num_para_palavras(numero, idioma):
    if numero in numeros_idiomas[idioma]:
        return numeros_idiomas[idioma][numero]
    elif numero < 100:
        dezena = numero // 10 * 10
        unidade = numero % 10
        return numeros_idiomas[idioma][dezena] + ("-" if unidade != 0 else "") + numeros_idiomas[idioma][unidade]
    elif numero < 1000:
        centena = numero // 100
        resto = numero % 100
        return numeros_idiomas[idioma][centena] + (" hundred " if resto != 0 else "") + num_para_palavras(resto, idioma)
    elif numero < 1000000:
        milhar = numero // 1000
        resto = numero % 1000
        return num_para_palavras(milhar, idioma) + (" thousand " if resto != 0 else "") + num_para_palavras(resto, idioma)

def num_para_extenso(numero, idioma):
    if idioma == 'en':
        try:
            return num_para_palavras(int(numero), idioma)
        except ValueError:
            return "Invalid number"
    else:
        return "This feature is not available for this language."

# Função para falar o número no idioma selecionado
def falar_numero(numero_palavras, idioma):
    tts = gTTS(text=numero_palavras, lang=idioma)
    tts.save("numero.mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("numero.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()

# Função para gerar um novo número e exibi-lo
def novo_numero():
    global numero_aleatorio
    global questoes_acertadas
    global max_questoes_acertadas
    global idioma_atual
    global dificuldade_atual
    global modo_escrita_ativo

    entrada.delete(0, tk.END)
    resultado.set("")

    if idioma.get() != idioma_atual or dificuldade.get() != dificuldade_atual:
        questoes_acertadas = 0
        max_questoes_acertadas = 0
        label_questoes_acertadas.config(text=f"Seguidas: {questoes_acertadas} / ", justify="left")
        label_max_questoes_acertadas.config(text=f"⭐Seguidas: {max_questoes_acertadas}", justify="right")


    idioma_atual = idioma.get()
    dificuldade_atual = dificuldade.get()

    if modo_jogo == "Numeros":
        if dificuldade.get() == "Fácil":
            numero_aleatorio = random.randint(1, 100)
        elif dificuldade.get() == "Médio":
            numero_aleatorio = random.randint(100, 1000)
        elif dificuldade.get() == "Difícil":
            numero_aleatorio = random.randint(1000, 1000000)

        idioma_selecionado = idioma.get()
        texto_numero.set(num_para_palavras(numero_aleatorio, idioma_selecionado))
        if falar_var.get() == 1:
            threading.Thread(target=falar_numero, args=(num_para_palavras(numero_aleatorio, idioma_selecionado), idioma_selecionado)).start()

    elif modo_jogo == "Escrita":
        numero_aleatorio = random.randint(1, 100)
        texto_numero.set(numero_aleatorio)
        modo_escrita_ativo = True

# Função para verificar a resposta do usuário
def verificar_resposta(event=None):
    global questoes_acertadas
    global max_questoes_acertadas
    global modo_escrita_ativo

    resposta = entrada.get().strip().lower()
    if modo_jogo == "Numeros":
        try:
            resposta_numero = int(resposta)
            if resposta_numero == numero_aleatorio:
                questoes_acertadas += 1
                if questoes_acertadas > max_questoes_acertadas:
                    max_questoes_acertadas = questoes_acertadas
                resultado.set("Correto!")
                root.after(1000, lambda: resultado.set(""))
                root.after(1000, novo_numero)

                if dificuldade.get() == "Difícil" and questoes_acertadas == 15:
                    messagebox.showinfo("🎉Parabéns!", "🎉Você memorizou todos os principais números!🎉")
                    questoes_acertadas = 0
                    label_questoes_acertadas.config(text=f"Seguidas: {questoes_acertadas} / ", justify="left")
                    max_questoes_acertadas = 0
                    label_max_questoes_acertadas.config(text=f"⭐Seguidas: {max_questoes_acertadas}", justify="right")

            else:
                questoes_acertadas = 0
                resultado.set(f"Errado! O número correto era: {numero_aleatorio}")
                root.after(2000, lambda: resultado.set(""))
                root.after(2000, novo_numero)
        except ValueError:
            resultado.set("Por favor, digite um número válido.")

    elif modo_jogo == "Escrita":
        resposta_esperada = num_para_palavras(numero_aleatorio, idioma.get()).lower()
        if resposta == resposta_esperada:
            questoes_acertadas += 1
            if questoes_acertadas > max_questoes_acertadas:
                max_questoes_acertadas = questoes_acertadas
            resultado.set("Correto!")
            root.after(1000, lambda: resultado.set(""))
            root.after(1000, novo_numero)
        else:
            resultado.set(f"Incorreto! A resposta correta era: {resposta_esperada}")

    label_questoes_acertadas.config(text=f"Seguidas: {questoes_acertadas} / ", justify="left")
    label_max_questoes_acertadas.config(text=f"⭐Seguidas: {max_questoes_acertadas}", justify="right")

# Função para fechar a janela
def fechar_janela():
    root.destroy()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Adivinhação de Números e Palavras")
root.attributes('-fullscreen', True)

# Adiciona um botão de fechar
btn_fechar = tk.Button(root, text="Fechar", command=fechar_janela)
btn_fechar.pack(side=tk.TOP, padx=10, pady=10)

texto_numero = tk.StringVar()
resultado = tk.StringVar()
idioma = tk.StringVar()
dificuldade = tk.StringVar()
falar_var = tk.IntVar()

idioma.set("en")
dificuldade.set("Fácil")

frame_superior = tk.Frame(root)
frame_superior.pack(pady=10)

frame_central = tk.Frame(root)
frame_central.pack(pady=10)

frame_inferior = tk.Frame(root)
frame_inferior.pack(pady=10)

label_titulo = tk.Label(frame_superior, text="Adivinhação de Números e Palavras", font=("Arial", 18))
label_titulo.pack()

label_numero = tk.Label(frame_central, textvariable=texto_numero, font=("Arial", 24))
label_numero.pack()

label_resultado = tk.Label(frame_central, textvariable=resultado, font=("Arial", 18))
label_resultado.pack()

label_questoes_acertadas = tk.Label(frame_inferior, text=f"Seguidas: {questoes_acertadas} / ", justify="left")
label_questoes_acertadas.pack(side=tk.LEFT)

label_max_questoes_acertadas = tk.Label(frame_inferior, text=f"⭐Seguidas: {max_questoes_acertadas}", justify="right")
label_max_questoes_acertadas.pack(side=tk.RIGHT)

entrada = tk.Entry(frame_central, font=("Arial", 18), width=10)
entrada.pack(pady=10)
entrada.bind("<Return>", verificar_resposta)

label_idioma = tk.Label(frame_superior, text="Escolha o Idioma:", font=("Arial", 14))
label_idioma.pack()

radiobtn_en = tk.Radiobutton(frame_superior, text="Inglês", variable=idioma, value="en")
radiobtn_en.pack(anchor=tk.W)
radiobtn_es = tk.Radiobutton(frame_superior, text="Espanhol", variable=idioma, value="es")
radiobtn_es.pack(anchor=tk.W)
radiobtn_fr = tk.Radiobutton(frame_superior, text="Francês", variable=idioma, value="fr")
radiobtn_fr.pack(anchor=tk.W)
radiobtn_de = tk.Radiobutton(frame_superior, text="Alemão", variable=idioma, value="de")
radiobtn_de.pack(anchor=tk.W)
radiobtn_it = tk.Radiobutton(frame_superior, text="Italiano", variable=idioma, value="it")
radiobtn_it.pack(anchor=tk.W)

label_dificuldade = tk.Label(frame_superior, text="Escolha a Dificuldade:", font=("Arial", 14))
label_dificuldade.pack()

radiobtn_facil = tk.Radiobutton(frame_superior, text="Fácil", variable=dificuldade, value="Fácil")
radiobtn_facil.pack(anchor=tk.W)
radiobtn_medio = tk.Radiobutton(frame_superior, text="Médio", variable=dificuldade, value="Médio")
radiobtn_medio.pack(anchor=tk.W)
radiobtn_dificil = tk.Radiobutton(frame_superior, text="Difícil", variable=dificuldade, value="Difícil")
radiobtn_dificil.pack(anchor=tk.W)

btn_novo_numero = tk.Button(frame_central, text="Novo Número", font=("Arial", 14), command=novo_numero)
btn_novo_numero.pack(pady=10)

btn_verificar_resposta = tk.Button(frame_central, text="Verificar Resposta", font=("Arial", 14), command=verificar_resposta)
btn_verificar_resposta.pack(pady=10)

chk_falar = tk.Checkbutton(frame_central, text="Falar número", variable=falar_var)
chk_falar.pack(pady=10)

# Inicializar a tela em modo Números
novo_numero()

root.mainloop()
