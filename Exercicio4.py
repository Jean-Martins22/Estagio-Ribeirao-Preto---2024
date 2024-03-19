'''
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?
'''

import time


def descobrir_interruptores_lampadas():
    # Liga o interruptor 1
    print("Ligando o primeiro interruptor...")
    time.sleep(2)  # Espera 2 segundos (simulando um tempo para observar)
    print("Desligando o primeiro interruptor...")

    # Liga o interruptor 2
    print("Ligando o segundo interruptor...")
    time.sleep(2)
    print("Indo verificar as lâmpadas...")

    # Observa as lâmpadas
    print("\nObservando as lâmpadas...")
    primeira_lampada = input("A primeira lâmpada está acesa? (sim/não): ")
    segunda_lampada = input("A segunda lâmpada está quente? (sim/não): ")

    if primeira_lampada.lower() == "sim":
        print("O primeiro interruptor controla a primeira lâmpada.")
        print("O segundo interruptor controla a segunda lâmpada.")
        print("O terceiro interruptor controla a terceira lâmpada.")
    elif segunda_lampada.lower() == "sim":
        print("O primeiro interruptor controla a segunda lâmpada.")
        print("O segundo interruptor controla a primeira lâmpada.")
        print("O terceiro interruptor controla a terceira lâmpada.")
    else:
        print("O primeiro interruptor controla a terceira lâmpada.")
        print("O segundo interruptor controla a primeira lâmpada.")
        print("O terceiro interruptor controla a segunda lâmpada.")


descobrir_interruptores_lampadas()
