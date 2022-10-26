# Objetivo: Faça um programa que leia o nome de uma cidade e escreva se tem ou não "Santo" no inicio do nome.
# Data: 21/10/22
# Author: Washington
print("{:-^50}".format("Inicio do Programa"), "\n")
cidade = str(input("Entre com o nome da cidade: ")).strip().upper()

print("A cidade informada foi : {}".format(cidade))
print("Existe 'Santo' no nome da cidade? {}".format("SANTO" in cidade[0:5]))

print("\n", "{:-^50}".format("Fim do Programa"))
