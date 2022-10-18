# Faça um programa que lê quanto de dinheiro uma pessoa tem na carteira e mostra seu valor em dólar.

dolar = 5.28 #em 18/10/22

montante = float(input("Quantos reais você tem na sua carteira: "))

montante_em_dolar = montante / dolar

print("O montante {} em reais é igual a {} em dolar".format(montante, montante_em_dolar))

print("\nFim do programa.")