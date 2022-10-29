# Objetivo:Escreva um programa que leia um número inteiro qualquer e mostre na tela os N primeiros
# elementos de uma sequencia Fibonacci.
# Data: 28/10/22
# Author: Washington

print("{:-^50}".format(" Sequência Fibonacci "), "\n")

# numero = int(input("Entre com um número inteiro: "))
elementos = int(input("Quantos elementos da sequência deseja imprimir ? "))

aux = 0
anterior = 1
atual = aux + anterior
contador = 1

print("{}, {}, {}".format(aux, anterior, atual), end="")

while contador <= elementos - 3:
    aux = anterior
    anterior = atual
    atual = aux + anterior
    contador += 1
    print(", {}".format(atual), end="")

print("\n", "{:-^50}".format("Fim do Programa"))
