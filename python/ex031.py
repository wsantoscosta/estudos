# Objetivo: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens longas.
# Data: 22/10/22
# Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

kilometragem = float(input("Entre com a distância a ser percorrida em Km : "))

if kilometragem <= 200.00:
    print("O valor a pagar será de R$ {:.2f}.".format(kilometragem * 0.50))
else:
    print("O valor a pagar será de R$ {:.2f}".format(kilometragem * 0.45))

print("\n", "{:-^50}".format("Fim do Programa"))
