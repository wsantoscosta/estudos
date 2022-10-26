# Objetivo: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor for impar desconsidere-o.
# Data: 26/10/22
# Author: Washington

print("{:-^50}".format(" Somando números pares "), "\n")

soma = 0

for i in range(1, 7):
    numero = int(input("Entre com o {}º numero: ".format(i)))
    if (numero % 2) == 0:
        soma += numero
        print("\033[32mNumero par: {}\033[m".format(numero))
print("Soma dos números pares digitados é {}".format(soma))

print("\n", "{:-^50}".format("Fim do Programa"))
