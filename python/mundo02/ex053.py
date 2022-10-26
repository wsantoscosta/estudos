# Objetivo: Crie um programa que leia uma frase qualquer e diga se ela é ou não um palíndromo. 
# Desconsiderando o espaços em branco.
# Data: 26/101/22
# Author: Washington

print("{:-^50}".format(" Teste de palídromo "), "\n")

frase = str(input('Entre com uma palavra ou frase: ')).replace(" ","").upper()

if frase == frase[::-1]:
    print("\033[32mA frase é um palíndromo.\033[m")
else:
    print("\033[31m A frase não é um palídromo.\033[m")

print(frase)
print(frase[::-1])

print("\n", "{:-^50}".format("Fim do Programa"))
