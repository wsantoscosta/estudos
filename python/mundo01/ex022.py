# Objetivo: Crie um programa que leia o nome completo de uma pessoa e mostre em:
# Maiúscula, minúscula, quantidade de letras e quantidade de letras do 1° nome.
# Data: 21/10/22
# Author: Washington
print("{:-^50}".format("Inicio do Programa"), "\n")

nome = str(input("Entre com seu nome completo: "))

print("""O nome digitado foi ==> {} \n
      Em maiúscula ==> {} \n 
      Em minúscula ==> {} \n 
      O nome tem {} letras e o primeiro nome tem {} letras."""
      .format(nome, nome.upper(), nome.lower(), len(nome.replace(" ", "")), nome.find(" ")))

print("\n", "{:-^50}".format("Fim do Programa"))
