# Objetivo: Faça um programa que leia um número qualquer e mostre o seu factorial.
# Data: 27/10/22
# Author: Washington

print("{:-^50}".format(" Cálculo Factorial "), "\n")

numero = int(input("Entre com um número inteiro: "))
contador = numero 
factorial = 1
expressao = ""
while contador > 0:
    factorial *=   contador
    expressao += str(contador) + (" X " if contador > 1 else " = ")
    contador -= 1 

print("O factorial do número {}! {} {}".format(numero,expressao, factorial))

print("\n", "{:-^50}".format("Fim do Programa"))
