# Objetivo: Refaça o desafio 9 mostrando a tabuada de um número que o usuário escolher, utilizando o laço for.
# Data: 26/10/22
# Author: Washington

print("{:-^50}".format(" Tabuada "), "\n")

numero = int(input("Entre com um numero: "))

for n in range(1, 11):
    print("{:>3}  x {:>3} = {:>3}".format(numero, n, numero * n))

print("\n", "{:-^50}".format("Fim do Programa"))
