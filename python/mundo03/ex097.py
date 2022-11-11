# Objetivo: Faça um programa que tenha uma função chamada escreve() que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.
# Data: 11/11/22
# Author: Washington

print(f"{' Tamanho adaptável ':-^50}", "\n")

def escreve(msg):
    print("-" * (len(msg) + 4))
    print(" ",msg)
    print("-" * (len(msg) + 4))

texto = str(input("Entre com um texto: ")).strip()

escreve(texto)


print("\n", f"{' Fim do Programa ':-^50}")

