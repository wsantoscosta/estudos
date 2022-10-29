# Objetivo: Crie um programa que leia vários números pelo teclado. 
# No final da execução mostre a média entre todos os valores e qual foi o maior e menor valor lido. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
# Data: 28/10/22
# Author: Washington

print("{:-^50}".format(" Lendo números e classificando-os "), "\n")
soma = 0
media = 0
maior = 0
menor = 0
numeros_lidos = 0
continua = "S"

while continua == "S":
    numero = float(input("Entre com um número: "))
    numeros_lidos += 1
    soma += numero

    if maior == 0:
        maior = numero
        menor = numero
        media = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    
    media = soma / numeros_lidos

    continua = str(input("Deseja continuar [S/N]? ")).strip().upper()

print("Para os números informados [ Total  {} ], temos Soma {:.2f}, média {:.2f}, maior {:.2f} e menor {:.2f}".format(numeros_lidos,soma, media, maior, menor))  

print("\n", "{:-^50}".format("Fim do Programa"))
