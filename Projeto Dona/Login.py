import customtkinter

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
        print('Acesso liberado')
    else:
        print('Acesso negado')

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
