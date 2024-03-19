'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
'''


def inverter_string(string):
    tamanho = len(string)
    string_invertida = ""
    for i in range(tamanho - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida


minha_string = "Estágio Ribeirão Preto!"

string_invertida = inverter_string(minha_string)

print("String invertida:", string_invertida)
