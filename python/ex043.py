# Objetivo: Desenvolva uma lógica que leia o peso e altura de uma pessoa e calcule o IMC e mostre seu
# status de acordo com a tabela: < 18.5 abaixo do peso, 25 peso ideal, 30 sobrepeso, 40 obesidade, > 40
# obesidade mórbida.
# Data: 25/10/22
# Author: Washington

print("{:-^50}".format("Cálculo do IMC - Índice de Massa Corporal"), "\n")

altura = float(input("Entre com a sua altura: "))
peso = float(input("Ente com seu peso: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Seu IMC é \033[33m{:.2f}\033[m, você está abaixo do peso ideal.".format(imc))
elif imc == 18.5 or imc < 25:
    print("Seu IMC é \033[32m{:.2f}\033[m, você está no peso ideal.".format(imc))
elif imc == 25 or imc < 30:
    print("Seu IMC é \033[31m{:.2f}\033[m, você está com sobrepeso!".format(imc))
elif imc == 30 or imc < 40:
    print("Seu IMC é \033[35m{:.2f}\033[m, você está com obesidade".format(imc))
else:
    print("Seu IMC é \033[1;31;43m{:.2f}\033[m, Você tem obessidade morbida!".format(imc))

print("\n", "{:-^50}".format("Fim do Programa"))
