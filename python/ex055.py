# Objetivo: Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e menor peso lido.
# Data: 26/10/22
# Author: Washington

print("{:-^50}".format(" Comparando pesos de cinco pessos "), "\n")

menor = 0.0
maior = 0.0

for p in range(1, 6):
    peso = float(input("Informe o {p}º peso : ".format(p)))
    if p == 1:
        menor = peso
        maior = peso
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso

print("\nO menor peso recebido foi \033[32m{:.1f}\033[m.".format(menor))
print("O maior peso recebido foi \033[31m{:.1f}\033[m".format(maior))

print("\n", "{:-^50}".format("Fim do Programa"))

