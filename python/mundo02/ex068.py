# Objetivo: Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quado o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
# Data: 31/10/22
# Author: Washington

from random import randint

print("{:-^50}".format(" Jogando par ou ímpar "), "\n")

vitorias = 0

while True:

    escolha = ""
    computador = randint(0, 10)
    jogador = int(input("Entre com um número entre 0 e 10: "))
    
    while escolha != "PAR" and escolha != "IMPAR":
        escolha = str(input("Escolha par ou ímpar: ")).strip().upper()

    if (jogador + computador ) % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "IMPAR"

    print(f"Resultado: computador  {computador} + você {jogador}  = {computador + jogador} ==> {resultado}")

    if resultado != escolha:
        break
    else:
        print(f"Você venceu....\n {' Próxima Rodada ':-^40}")
        vitorias += 1

print(f"Você perdeu patinho... Mas teve {vitorias} vitórias.")

print("\n", "{:-^50}".format("Fim do Programa"))
