'''
3) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____
'''

# Sequência a) 1, 3, 5, 7, ___
sequencia_a = [1, 3, 5, 7]
proximo_elemento_a = sequencia_a[-1] + 2
print("Próximo elemento da sequência a):", proximo_elemento_a)

# Sequência b) 2, 4, 8, 16, 32, 64, ____
sequencia_b = [2, 4, 8, 16, 32, 64]
proximo_elemento_b = sequencia_b[-1] * 2
print("Próximo elemento da sequência b):", proximo_elemento_b)

# Sequência c) 0, 1, 4, 9, 16, 25, 36, ____
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
proximo_elemento_c = len(sequencia_c) ** 2
print("Próximo elemento da sequência c):", proximo_elemento_c)

# Sequência d) 4, 16, 36, 64, ____
sequencia = [4, 16, 36, 64]
proximo_numero = 10 ** 2
print("O próximo número da sequência é:", proximo_numero)

# Sequência e) 1, 1, 2, 3, 5, 8, ____
sequencia_e = [1, 1, 2, 3, 5, 8]
proximo_elemento_e = sequencia_e[-1] + sequencia_e[-2]
print("Próximo elemento da sequência e):", proximo_elemento_e)

# Sequeência f) 2, 10, 12, 16, 17, 18, 19, ____ ?
