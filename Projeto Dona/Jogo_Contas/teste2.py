string = "100abc e 2"
numero = ""
for caractere in string:
    if caractere.isdigit():
        numero += caractere
    else:
        break
print(numero)