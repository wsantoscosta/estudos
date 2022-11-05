# Objetivo: Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. 
# No final: qtde de pessoas, pessoas mais pesadas > 100 , mais leves <= 70.
# Data: 04/11/22
# Author: Washington

print(f"{' Gravando pessoas em lista ':-^50}", "\n")
pessoas = []

while True:

    continua = " "

    pessoas.append(str(input("Entre com o nome da pesssoa: ")))
    pessoas.append(float(input("Entre com o peso da pessoa: ")))

    print("-" * 50)

    while continua not in 'SN':
        
        continua = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]

    if continua == "N":
        break
    
    print("-" * 50)

print(f"Ao todo você cadastrou {int(len(pessoas) / 2)} pessoas.")

print(f"As pessoas mais pessadas foram : ", end=" ")
for indice, valor in enumerate(pessoas):
    
    if (indice % 2) != 0:
        if valor >= 100:
            print(pessoas[indice - 1], end=" ")
        

print(f"\nAs pessoas mais leves foram: ", end="")
for indice, valor in enumerate(pessoas):
    
    if (indice % 2) != 0:
        if valor <= 70:
            print(pessoas[indice - 1], end=" ")

print("\n", f"{' Fim do Programa ':-^50}")
