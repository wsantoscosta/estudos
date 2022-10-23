# Objetivo: Desenvolva um programa que leia o comprimento de três retas e informe ao usuário se elas podem ou não formar um triângulo.
# Data: 23/10/22
# Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

reta1 = float(input("Entre com o comprimento da primeira reta  : "))
reta2 = float(input("Entre com o comprimento da segunda reta  : "))
reta3 = float(input("Entre com o comprimento da terceira reta   : "))

if (reta1 + reta2 > reta3) and (reta1 + reta3  > reta2) and (reta2 + reta3 > reta1):
    print("Com os comprimentos de reta informados é possível formar um triângulo.")
else:
    print("Com os comprimentos de reta informados não é possível formar um triângulo.")

print("\n", "{:-^50}".format("Fim do Programa"))
