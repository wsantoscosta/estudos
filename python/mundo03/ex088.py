# Objetivo: Faça um programa que ajude um jogador da mega sena a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear seis número entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.
# Data: 04/11/22
# Author: Washington
from random import sample
from time import sleep

print(f"{' Gerador de palpites para Mega Sena ':-^50}", "\n")

palpites = []
numeros = []

for i in range(1, 61):
    numeros.append(i)

jogos = int(input("Quantos palpites deseja gerar: "))

for n in range(0, jogos):
    palpites.append(sample(numeros, k=6))
    palpites[n].sort()
    print(f"Gerando jogo {n + 1}...{palpites[n]}")
    sleep(1)  

#print(palpites)
print("\033[42mBoa Sorte!\033[m")
print("\n", f"{' Fim do Programa ':-^50}")