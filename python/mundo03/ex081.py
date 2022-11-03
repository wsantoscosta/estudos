# Objetivo: Crie um programa que vai ler vários números e colocar em uma lista depois disso:
# qtde números digitados, a lista em ordem decrescente e se o número 5 está ou não na lista
# Data: 03/11/22
# Author: Washington

numeros = []

print(f"{' Inserindo números em lista ':-^50}", "\n")

while True:

    continua = ' '
    numero = int(input("Entre com um número: "))
    numeros.append(numero)

    while continua not in 'SN':
        continua = str(input("Deseja continuar? [S/N] ")).strip().upper()
        
    if continua == "N":
        break

numeros.sort(reverse=True)
print("-" * 50)
print(f"\nA quantidade de números digitados foi : {len(numeros)}.")
print(f"A lista em ordem decrescente é {numeros}.")

if 5 in numeros:
    print(f"O número 5 está na lista na posição: {numeros.index(5)}.")
else:
    print("O número 5 não foi encontrado na lista.")

print("\n", f"{' Fim do Programa ':-^50}")