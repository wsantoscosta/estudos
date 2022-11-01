# Objetivo: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que está na tupla.
# Data: 01/11/22
# Author: Washington
from random import randint

print(f"{' Gerando números em tuplas ':-^50}", "\n")

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

maior = numeros[0]
menor = numeros[0]

# com metodo ==> min(menor) / min(numeros)
for x in numeros:
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    
for n in numeros:
    print(f"{n} ", end="")

print()
print(f"O maior número é {maior} e o menor é {menor}")

print("\n", f"{' Fim do Programa ':-^50}")