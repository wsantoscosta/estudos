# Objetivo: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Data: 26/10/22
# Author: Washington

print("{:-^50}".format(" Checando número primo "), "\n")
teste = 0
numero = int(input("Entre com um número inteiro: "))

for i in range((numero -1), 1, -1): # Checar se existe algum divisor entre 1 e o número informado 
    if numero % i == 0:
        teste = 1
if teste == 0:
    print("\033[32mO número {} é um número primo! \033[m".format(numero))
else:
    print("\033[31mO número {} não é um número primo!\033[m".format(numero))

print("\n", "{:-^50}".format("Fim do Programa"))