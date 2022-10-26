# Objetivo: Crie um programa que leia um número inteiro e mostre se é par ou impar.
# Data: 23/10/22
# Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

numero = int(input("Entre com um número inteiro: "))

if numero % 2 == 0:
    print("0 número é par.")
else:
    print("O número é impar.")

print("\n", "{:-^50}".format("Fim do Programa"))