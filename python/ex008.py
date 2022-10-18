# Faça um programa que lê um valor em metros e o exibe convertido em centímetros e milímetros.

medida = int(input("Entre com uma medida em metros: "))

print("A medida digitada foi {} metros ".format(medida))
print("Seu valor em centímetros é {}".format(medida * 100))
print("Seu valor em milímetros é {}".format(medida * 1000))

print("\nFim do programa.")