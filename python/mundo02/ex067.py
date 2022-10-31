# Objetivo: 067 - Faça um programa que mostre a tabuada de vários números um de cada vez para cada valor
# digitado pelo usuário. O programa será interrompido quando o valor solicitado for negativo.
# Data: 31/10/22
# Author: Washington

print("{:-^50}".format(" Imprimindo tabuadas "), "\n")

while True:

    numero = int(input("Entre com um número: "))
    
    if numero < 0:
        break

    for x in range(1, 11):
        print(f"{numero:>} x {x:>2} = {numero * x:>5}")
    
    print(f"{' Fim da tabuada ' :-^50}")

print("\n", "{:-^50}".format("Fim do Programa"))