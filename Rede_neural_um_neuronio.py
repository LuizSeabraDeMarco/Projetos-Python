import math

input = 1
out_de = 0

input_wei = 0.5

learning_rate = 0.1

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

print("entrada", input, "desejado", out_de)
erro = math.inf

interation = 0
while not erro ==0:
    interation += 1
    print("Interacao: ", interation)
    print('peso', input_wei)
    sum = input * input_wei
    sum = input * input_wei

    output = activation(sum)

    print(output)

    erro = out_de - output

    print("Erro", erro)

    if not erro == 0:
        input_wei = input_wei + learning_rate * input * erro

print('Parabens')