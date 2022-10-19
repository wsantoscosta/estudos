# Objetivo: Faça um programa que lê uma temperatura em Celsius e converte para Fahrenheit.
# Data: 18/10/22
#Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

temperatura_celcius = float(input("Entre com a temperatura em graus Celcius: ° "))
temperatura_fahrenheit = (temperatura_celcius * 9 / 5) + 32

print("A temperatura informada foi {}°C, o valor em fahrenheit é {}°F".format(temperatura_celcius, temperatura_fahrenheit), "\n")

print("{:-^50}".format("Fim do Programa"))