# Objetivo: Faça um programa que leia três números e mostre qual é o maior e o menor.
# Data: 22/10/22
# Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

num1 = float(input("Entre com o primeiro número: "))
num2 = float(input("Entre com o segundo número: "))
num3 = float(input("Entre com o terceiro número: "))

maior = num1
menor = num1

#if num1 > num2 and num1 > num3:
 #   maior = num1
if num2 > num3 and num2 > num1:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
#if num1 < num2 and num1 < num3:
 #   menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print('Dos numeros digitados o menor é {} e o maior é {}'.format(menor, maior))

print("\n", "{:-^50}".format("Fim do Programa"))