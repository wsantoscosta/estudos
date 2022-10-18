# Faça um programa que lêia um número inteiro qualquer e mostra sua tabuada.

numero = int(input("Entre com um numéro inteiro: "))
print("===========")

for i in range(1,11):
    print("{} x {:>2} = {:>2}".format(numero, i, numero * i))

print("===========")

print("\nFim do programa.")   