# Objetivo: Faça um programa que leia o comprimento do cateto oposta e cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.
# Data: 19/10/22
# Author: Washington

from math import hypot, sqrt

print("{:-^50}".format("Inicio do Programa"), "\n")

cateto_oposto = float(input("Entre com a medida do cateto oposto: "))
cateto_adjacente = float(input("Entre com a medida do cateto adjacente: ")) 
hipotenusa = sqrt((cateto_oposto ** 2 ) + (cateto_adjacente ** 2 ))

# ou hipotenusa = hypot(cateto_oposto, cateto_adjacente) 

print("Para os catetos: Oposto: {}, Adjacente: {} A Hipotenusa é {:.2f}"
      .format(cateto_oposto, cateto_adjacente, hipotenusa))

print("\n", "{:-^50}".format("Fim do Programa"))