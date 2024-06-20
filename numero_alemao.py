import tkinter as tk
from tkinter import messagebox
import random
from gtts import gTTS
import pygame
import pygame.mixer
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

# Variáveis globais para contagem de questões acertadas
questoes_acertadas = 0
max_questoes_acertadas = 0
idioma_atual = ""
dificuldade_atual = ""

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

# Função para falar o número no idioma selecionado
def falar_numero(numero_palavras, idioma):
    tts = gTTS(text=numero_palavras, lang=idioma)
    tts.save("numero.mp3")
    
    pygame.mixer.init()  # Initialize pygame mixer
    pygame.mixer.music.load("numero.mp3")  # Load the audio file
    pygame.mixer.music.play()  # Play the loaded audio

    while pygame.mixer.music.get_busy():  # Wait for the audio to finish playing
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()  # Quit pygame mixer after playback


# Função para gerar um novo número e exibi-lo
def novo_numero():
    global numero_aleatorio
    global questoes_acertadas
    global max_questoes_acertadas
    global idioma_atual
    global dificuldade_atual

    entrada.delete(0, tk.END)  # Limpa a caixa de entrada
    resultado.set("")  # Limpa o resultado anterior

    # Verifica se houve mudança no idioma ou dificuldade
    if idioma.get() != idioma_atual or dificuldade.get() != dificuldade_atual:
        questoes_acertadas = 0
        max_questoes_acertadas = 0
        label_questoes_acertadas.config(text="Seguidas: 0")
        label_max_questoes_acertadas.config(text="Máximo de Questões Seguidas: 0")

    idioma_atual = idioma.get()
    dificuldade_atual = dificuldade.get()

    if dificuldade.get() == "Fácil":
        numero_aleatorio = random.randint(1, 100)
    elif dificuldade.get() == "Médio":
        numero_aleatorio = random.randint(100, 1000)
    elif dificuldade.get() == "Difícil":
        numero_aleatorio = random.randint(1000, 1000000)

    idioma_selecionado = idioma.get()
    texto_numero.set(num_para_palavras(numero_aleatorio, idioma_selecionado))

    # Usar threading para falar o número em paralelo
    thread_audio = threading.Thread(target=falar_numero, args=(num_para_palavras(numero_aleatorio, idioma_selecionado), idioma_selecionado))
    thread_audio.start()

# Função para verificar a resposta do jogador
def verificar_resposta(event=None):
    global questoes_acertadas
    global max_questoes_acertadas

    resposta = entrada.get()
    try:
        resposta_numero = int(resposta)
        if resposta_numero == numero_aleatorio:
            questoes_acertadas += 1
            if questoes_acertadas > max_questoes_acertadas:
                max_questoes_acertadas = questoes_acertadas
            resultado.set("Correto!")
            root.after(1000, lambda: resultado.set(""))  # Limpa o resultado após 1 segundo
            root.after(1000, novo_numero)  # Espera 1 segundo e sorteia um novo número
            
            # Verifica se alcançou 15 acertos seguidos no nível Difícil
            if dificuldade.get() == "Difícil" and questoes_acertadas == 15:
                messagebox.showinfo("🎉Parabéns!", "🎉Você memorizou todos os principais números!🎉")
                questoes_acertadas = 0
                max_questoes_acertadas = 0
                label_questoes_acertadas.config(text="Questões Seguidas Acertadas: 0")
                label_max_questoes_acertadas.config(text="Máximo de Questões Seguidas Acertadas: 0")
        
        else:
            if dificuldade.get() == "Difícil":
                questoes_acertadas = 0
                resultado.set(f"Errado! O número correto era: {numero_aleatorio}")
                root.after(6000, lambda: resultado.set(""))  # Limpa o resultado após 2 segundos
                root.after(6000, novo_numero)  # Espera 2 segundos e sorteia um novo número
            else:
                questoes_acertadas = 0
                resultado.set(f"Errado! O número correto era: {numero_aleatorio}")
                root.after(2000, lambda: resultado.set(""))  # Limpa o resultado após 2 segundos
                root.after(2000, novo_numero)  # Espera 2 segundos e sorteia um novo número
    except ValueError:
        resultado.set("Por favor, digite um número válido.")

# Criando a interface gráfica
root = tk.Tk()
root.title("Jogo de Memória de Números por Extensão")

# Frame para seleção de idioma e dificuldade
frame_selecao = tk.Frame(root)
frame_selecao.pack(pady=10)

# OptionMenu para selecionar o idioma
tk.Label(frame_selecao, text="Selecione o idioma:").pack()
idioma = tk.StringVar()
idioma.set("de")  # Valor padrão
tk.OptionMenu(frame_selecao, idioma, "de", "fr", "en", "es").pack()

# OptionMenu para selecionar a dificuldade
tk.Label(frame_selecao, text="Selecione a dificuldade:").pack()
dificuldade = tk.StringVar()
dificuldade.set("Fácil")  # Valor padrão
tk.OptionMenu(frame_selecao, dificuldade, "Fácil", "Médio", "Difícil").pack()

# Frames para exibir o número, entrada de texto, resultado e contagem
frame_numero = tk.Frame(root)
frame_numero.pack(pady=10)
texto_numero = tk.StringVar()
label_numero = tk.Label(frame_numero, textvariable=texto_numero, font=("Helvetica", 24))
label_numero.pack()

frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)
entrada = tk.Entry(frame_entrada, font=("Helvetica", 18))
entrada.pack()
entrada.bind("<Return>", verificar_resposta)

frame_resultado = tk.Frame(root)
frame_resultado.pack(pady=10)
resultado = tk.StringVar()
label_resultado = tk.Label(frame_resultado, textvariable=resultado, font=("Helvetica", 18))
label_resultado.pack()

frame_contagem = tk.Frame(root)
frame_contagem.pack(pady=10)
label_questoes_acertadas = tk.Label(frame_contagem, text="Questões Seguidas Acertadas: 0", font=("Helvetica", 14))
label_questoes_acertadas.pack()
label_max_questoes_acertadas = tk.Label(frame_contagem, text="Máximo de Questões Seguidas Acertadas: 0", font=("Helvetica", 14))
label_max_questoes_acertadas.pack()

# Botões
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)
botao_novo = tk.Button(frame_botoes, text="Novo Número", command=novo_numero, font=("Helvetica", 14))
botao_novo.pack(side=tk.LEFT, padx=10)
botao_verificar = tk.Button(frame_botoes, text="Verificar", command=verificar_resposta, font=("Helvetica", 14))
botao_verificar.pack(side=tk.RIGHT, padx=10)

# Função para atualizar a contagem de questões acertadas
def atualizar_contagem():
    global questoes_acertadas
    global max_questoes_acertadas

    label_questoes_acertadas.config(text=f"Seguidas: {questoes_acertadas}")
    label_max_questoes_acertadas.config(text=f"⭐Seguidas: {max_questoes_acertadas}")
    root.after(100, atualizar_contagem)

atualizar_contagem()

# Iniciar com um número aleatório
novo_numero()

# Executar a interface gráfica
root.mainloop()
