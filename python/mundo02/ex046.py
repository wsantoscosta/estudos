# Objetivo: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
# artifícios, indo de 10 até 0 com uma pausa de 1 segundo entre eles.
# Data: 26/10/22
# Author: Washington

import emoji
from time import sleep

print("{:-^50}".format("Contagem regressiva"), "\n")

for n in range(10, -1, -1):
    print( "." * n,     "{}".format(n) )
    sleep(1)
print(emoji.emojize(':fireworks:') * 10 )

print("\n", "{:-^50}".format("Fim do Programa"))
