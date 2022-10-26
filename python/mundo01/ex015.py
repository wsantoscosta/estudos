# Objetivo:Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia mais R$ 0,15 por km rodado.
# Data: 18/10/22
# Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

km_percorridos = float(input("Informe quantos quilômetros foram percorridos: "))
dias_utilizados = int(input("Informe por quantos dias o carro foi utilizado: "))

valor_pagar = (km_percorridos * 0.15) + (dias_utilizados * 60.00)

print("O veículo foi utilizado por {} dias e percorreu {} km, o valor a pagar é de R$ {:.2f}"
      .format(dias_utilizados, km_percorridos, valor_pagar), "\n")

print("{:-^50}".format("Fim do Programa"))