# Objetivo: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a
# mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda()
# desenvolvido no desafio 108.
# Data: 15/11/22
# Author: Washington

from ex109 import moeda

print(f"{' Módulos e funções ':-^50}", "\n")

numero = float(input("Entre com um número: "))

print(f"A metade de {numero} é {moeda.metade(numero)}")
print(f"O dobro de {numero} é {moeda.dobro(numero)}")
print(f"Com aumento de 15% : {numero} é {moeda.aumentar(numero, 15, True)}")
print(f"Com desconto de 25% : {numero} é {moeda.diminuir(numero, 25, True)}")

print("\n", f"{' Fim do Programa ':-^50}")