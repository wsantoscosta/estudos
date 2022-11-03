# Objetivo: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final mostre o maior, o menor e as suas respectivas posições.
# Data: 03/11/22
# Author: Washington

print(f"{' Analisando números em lista ':-^50}", "\n")

lista = []
p_maiores = []
p_menores = []

for x in range(1, 6):
   
    num = int(input(f"Entre com o {x}º número: "))
    lista.append(num)
    
print("-" * 50)

print(f"\nO maior número é {max(lista)} e está nas posições ", end="")

for pos, valor in enumerate(lista):
    if valor == max(lista):
        print(f"{pos + 1}", end=" ")

print(f"\nO menor número é {min(lista)} e está nas posições ", end="")

for pos, valor in enumerate(lista):
    if valor == min(lista):
        print(f"{pos + 1}", end=" ")

print("\n", f"{' Fim do Programa ':-^50}")
