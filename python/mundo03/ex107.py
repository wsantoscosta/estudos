# Objetivo: Crie um módulo chamado moedapy que tenha as funções aumentar(), diminuir(), dobro() e
# metade(). Faça um programa que importe esse módulo e use algumas dessas funções.
# Data: 15/11/22
# Author: Washington

from ex107 import moeda

print(f"{' Utilizando módulos próprios ':-^50}", "\n")

numero = float(input("Entre com um número: "))
print(f"A metade de {numero} é {moeda.metade(numero):.2f}")
print(f"O dobro de {numero} é {moeda.dobro(numero):.2f}")
print(f"Aumentando em 10% temos {moeda.aumentar(numero, 10):.2f}")
print(f"Com desconto de 30% temos {moeda.diminuir(numero, 30):.2f}")

print("\n", f"{' Fim do Programa ':-^50}")