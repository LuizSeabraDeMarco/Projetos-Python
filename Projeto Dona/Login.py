import customtkinter
from Falar import comprimento
from jogo import conta
from Pergunta_fala import fala
import speech_recognition as sr


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

nome = customtkinter.CTkEntry(janela, placeholder_text="Seu nome")
nome.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

def clique():
    if nome.get() == 'Luiz' and senha.get() == 'stark':
        comprimento()
        janela.destroy()
        from menu import roda
        from menu import opcao
        from menu import espaco
        roda()
    else:
        print('Acesso negado')

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
