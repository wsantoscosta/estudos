# Objetivo: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar 999, que é a condição de parada. 
# No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).
# Data: 28/10/22
# Author: Washington

print("{:-^50}".format(" Lendo números "), "\n")

total_digitado = 0
soma = 0
numero = 0

while numero != 999:
  
    numero = int(input("Entre com um número (999 para encerrar) : "))
    
    if numero != 999:
        total_digitado +=1
        soma += numero

print("O Total de números digitados foi: {} somando {}".format(total_digitado, soma))

print("\n", "{:-^50}".format("Fim do Programa"))