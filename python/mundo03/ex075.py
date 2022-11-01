# Objetivo: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em um tupla, 
# no final mostre quantas vezes apareceu o número 9, em que posição aparece o número 3 e quais são pares.
# Data: 01/11/22
# Author: Washington

print(f"{' Analisando números em tuplas ':-^50}", "\n")
pares = ""

# or num = (int(input()), int(input()), .....)
num1 = int(input("Entre com um numero: "))
num2 = int(input("Entre com um numero: "))
num3 = int(input("Entre com um numero: "))
num4 = int(input("Entre com um numero: "))

numeros = (num1, num2, num3, num4)
print("Os números na tupla são: ", numeros)

if numeros.count(9) <= 0:
    print("Não foi encontrado o número 9 na tupla.")
else:
    print(f"O número 9 apareceu {numeros.count(9)} vez(es) na tupla.")

if  3 not in numeros:
    print("Não foi encontrado o número 3 na tupla")
else:
    print("O número 3 aparece na poosição: ", numeros.index(3) + 1)

for x in numeros:
    if x % 2 == 0:
        pares += " " + str(x)

if pares == "":
    print("Não foram encontrados números pares na tupla.")
else:
    print(f"Os números pares encontrados foram: {pares}.")

print("\n", f"{' Fim do Programa ':-^50}")
