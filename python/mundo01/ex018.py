# Objetivo: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo.
# Data: 19/10/22
# Author: Washington

from math import cos, sin, tan, radians 
print("{:-^50}".format("Inicio do Programa"), "\n")

angulo = int(input("Entre com a medida do angulo: "))

radiano = radians(angulo)

# print("Angulo {} ---- Radiano {}".format(angulo, radiano))

print("Para o ângulo de {}°, O Seno é {:.2f}, Cosseno {:.2f} e a Tangente {:.2f}."
     .format(angulo, sin(radiano), cos(radiano), tan(radiano)))

print("\n", "{:-^50}".format("Fim do Programa"))