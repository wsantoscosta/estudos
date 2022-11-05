# Objetivo: Crie um programa que crie uma matriz de 3 x 3 e preencha com os valores lidos pelo teclado.
# No final mostre a matriz com a formatação correta.
# Data: 04/11/22
# Author: Washington

print(f"{' Criando uma matriz com listas ':-^50}", "\n")

matriz = [[], [],[]]

for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(f"Entre com um número para posição [{x} x {y}]: "))
        matriz[x].insert(y, num)

print("-" * 50)
for x in range(0, 3):
    print(f"{matriz[x]}")

print("\n", f"{' Fim do Programa ':-^50}")
