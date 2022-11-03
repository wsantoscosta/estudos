# Objetivo: Crie um programa que vai ler vários números e colocar em uma lista depois disso crie duas
# listas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente.
# Ao final mostre o conteúdo das três listas.
# Data: 02/11/22
# Author: Washington

print(f"{' Criando listas ' :-^50}", "\n")

lista = []
pares = []
impares = []

while True:
    continua = ' '

    valor = int(input("Entre com um valor: "))
    lista.append(valor)

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    
    while continua not in 'SN':
        continua = str(input("Deseja continuar? [S/N]")).strip().upper()[0]

    if continua == "N":
        break

print("-" * 50)

print(f"A lista geral contém os valores :\033[34m {lista}\033[m.")
print(f"A lista dos pares contém os valores:\033[32m {pares}\033[m.")
print(f"A lista dos ímpares contém os valores:\033[33m {impares}\033[m.")

print("\n", f"{' Fim do Programa ':-^50}")
