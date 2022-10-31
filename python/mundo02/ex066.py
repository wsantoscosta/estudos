# Objetivo: Crie um programa que leia vários números inteiros pelo teclado. Obs. 64  com Break e F-String
# O programa só vai parar quando o usuário digitar 999, que é a condição de parada. 
# No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).
# Data: 31/10/22
# Author: Washington

print("{:-^50}".format(" Lendo números "), "\n")

total_digitado = 0
soma = 0

while True:
    numero = float(input("Entre com um número: "))

    if numero == 999:
        break

    total_digitado +=1
    soma += numero

print(f"O Total de números digitados foi: {total_digitado} somando {soma}")