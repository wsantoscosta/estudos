# Objetivo: 047 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# Data: 26/10/22
# Author: Washington

print("{:-^50}".format("Mostrando os números pares entre 1 e 50"), "\n")

# for p in range(1, 51): ==> mais execuções do laço
for p in range(2, 51, 2):
    if (p % 2) != 1:
        print(">", p, end=" ")

print("\n", "{:-^50}".format("Fim do Programa"))
