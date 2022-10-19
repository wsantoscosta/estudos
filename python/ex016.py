# Objetivo: Crie um programa que leia um numero real qualquer e mostre na tela sua porção inteira.
# Data: 19/10/22
#Author: Washington

from math import trunc

print("{:-^50}".format("Inicio do Programa"), "\n")

numero_real = float(input("Entre com um número real: "))

print("O número digitado foi {} e sua porção inteira é {}".format(numero_real, trunc(numero_real)), "\n")

print("{:-^50}".format("Fim do Programa"))