# Objetivo: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Data: 22/10/22
# Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

ano = int(input("Entre com o ano a ser verificado: "))

if (ano % 4)  == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é Bissexto.".format(ano))
else:
    print("O ano {} não é Bissexto.".format(ano))

print("\n", "{:-^50}".format("Fim do Programa"))
