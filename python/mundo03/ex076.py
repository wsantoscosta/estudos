# Objetivo: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços em sequencia.
# No final mostre uma listagem de preços organizando os dados em forma tabular.
# Data: 01/11/22
# Author: Washington

print(f"{' Listagem de Preços ':-^50}", "\n")

lista = ("Caneta", 2.00, "Lápis", 1.50, "Borracha", 1.50, "Régua", 2.75, "Caderno", 15.00, "Estojo", 10.0)

print(f"\033[32m{'Produto':<20}{'Preço R$':^15}\033[m")

for p,i in enumerate(lista):
    if p % 2 == 0:
        print(f"{i:<20}", end="")
    else:
        print(f"{i:>10.2f}")

print("\n", f"{' Fim do Programa ':-^50}")
