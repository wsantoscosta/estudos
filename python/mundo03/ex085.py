# Objetivo: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e impares. no final mostre os valores pares e impares em ordem crescente.
# Data: 04/11/22
# Author: Washington


print(f"{' Lista de pares e ímpares ':-^50}", "\n")

pares = []
impares = []
lista_geral = [pares, impares]

for x in range(1, 8):
    num = int(input(f"Entre com o {x}º número: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
pares.sort()
impares.sort()

print("-" * 50)

print(f"A lista geral é: {lista_geral}")
print(f"A lista dos númeors pares é : {pares}")
print(f"A lista dos números ímpares é: {impares}")

print("\n", f"{' Fim do Programa ':-^50}")
