# Objetivo: Faça um programa que leia o nome completo de um a pessoa mostrado em seguida o primeiro e 0
# último nome separadamente.
# Data: 21/10/22
# Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

nome = str(input("Entre com o nome completo da pessoa: ")).strip()
print('Seu primeiro nome é: {}'.format(nome.split()[0]))
print('Seu último nome é: {}'.format(nome.split()[-1]))


print("\n", "{:-^50}".format("Fim do Programa"))
