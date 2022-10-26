# Objetivo: Escreva um programa que faça o computador "Pensar" em um número inteiro. Entre 0 e 5.
# Peça para o usuário tentar descobrir qual número foi escolhido pelo computador.
# Data: 23/10/22
# Author: Washington

from random import randint

print("{:-^50}".format("Inicio do Programa"), "\n")

numero_sorteado = randint(0, 5)

palpite = int(input("O computador sorteou um número. Dê seu palpite entre 0 e 5: "))

if numero_sorteado == palpite:
    print("Você acertou parabéns.")
else:
    print("Você errou.Tente outra vez.")

print("O número sorteado foi {}".format(numero_sorteado))

print("\n", "{:-^50}".format("Fim do Programa"))
