string = "123abc"
numero = ""
for caractere in string:
    if caractere.isdigit():
        numero += caractere
print(numero)