# Objetivo: Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
# Data: 21/10/22
# Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

pessoa = str(input('Digite seu nome completo: ')).strip().upper()
print('Silva contem no nome', 'SILVA' in pessoa)

print("\n", "{:-^50}".format("Fim do Programa"))
