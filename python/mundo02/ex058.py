# Objetivo:  Melhore o jogo do desafio 28 onde o computador vai pensar um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar. Mostrando no final quantos palpites foram necessários para vencer.
# Data: 27/10/22
# Author: Washington

from random import randint
from time import sleep

print("{:-^50}".format("Início do Programa"), "\n")

venceu = False
total_palpites = 1

while venceu == False:
    palpite = int(input("Entre com seu palpite entre 0 e 10: "))
    print("Computador pensando.......")
    sleep(2)
    computador = randint(0,10)

    if computador == palpite:
        print("\033[42mParabéns você venceu!!!\033[m")
        venceu = True
    else:
        print("\033[41mChupa! Você perdeu. hehehehe!\033[m")
        total_palpites += 1
    print("Jogador escolheu: {} \nComputador sorteou: {}".format(palpite, computador))

print("Você precisou de {} palpites para vencer.".format(total_palpites))

print("\n", "{:-^50}".format("Fim do Programa"))