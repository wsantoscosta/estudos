# Objetivo: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.
# Data: 26/10/22
# Author: Washington

print("{:-^50}".format("Calculando a PA - Progressão Aritmética"), "\n")

termo = int(input("Entre com o 1º termo da PA: "))
razao = int(input("Entre com a razão da PA: "))

print(50 * "-")

# n termo da PA = primeiro + (n -1 ) * razao

for i in range(1, 11):
    print("{:>3}º Termo da PA: {:>4}".format(i, termo))
    termo = termo + razao

print("\n", "{:-^50}".format("Fim do Programa"))
