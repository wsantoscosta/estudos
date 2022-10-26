# Objetivo: Faça um programa que leia um número entre 0 e 9999 e mostre na tela cada um dos dígitos:
# unidade, dezena , centena e milhar.
# Data: 21/10/22 
# Author: Washington
print("{:-^50}".format("Inicio do Programa"), "\n")

numero = int(input("Entre com um número entre 0 e 9999: "))

print('A unidade do número é : {}'.format(numero % 10))
print('A dezena do número é  : {}'.format(numero % 100 // 10))
print('A centena do número é : {}'.format(numero % 1000 // 100))
print('A milhar do número é  : {}'.format(numero % 10000 // 1000))


print("\n", "{:-^50}".format("Fim do Programa"))
