# Objetivo: Adapte o código do desafio 107 criando uma função adicional chamada moeda() que consiga
# mostrar os valores como um valor monetário formatado.
# Data: 15/11/22
# Author: Washington

from ex108 import moeda

print(f"{'Formatando valores monetários ':-^50}", "\n")

numero = float(input("Entre com um número: "))
print(f"O número {numero} formatado é {moeda.moeda(numero)}")
print(f"O dobro do número {numero} formatado é {moeda.moeda(moeda.dobro(numero))}")


print("\n", f"{' Fim do Programa ':-^50}")
