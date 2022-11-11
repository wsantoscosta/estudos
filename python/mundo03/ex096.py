# Objetivo: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.
# Data: 11/11/22
# Author: Washington
print(f"{' Cálculo da área ':-^50}", "\n")

def area(c, l):
    a = c * l
    print(f"A área do terreno de {c} x {l} é {a}m²")

comprimento = float(input("Entre com o compirmento do terreno (m): "))
largura = float(input("Entre com a largura do terreno (m): "))

print("-" * 50)

area(comprimento, largura)


print("\n", f"{' Fim do Programa ':-^50}")