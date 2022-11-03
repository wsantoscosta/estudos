# Objetivo: Crie um programam onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
# lista já na posição correta de inserção ( sem usar o sort). No final mostre a lista ordenada na tela. 
# Data: 03/11/22
# Author: Washington

print(f"{' Inserindo números em lista - em ordem ':-^50}", "\n")

numeros = []
msg = "O número foi adicionado na posição: "

for x in range(0, 5):
    numero = int(input(f"Entre com o {x}º número: "))
    
    if x == 0:
        numeros.append(numero)
    else:    
        if numero > max(numeros):
            numeros.append(numero)
        elif numero < min(numeros):
            numeros.insert(0, numero)
        elif numero <= numeros[1]:
            numeros.insert(1, numero)
        elif numero <= numeros[2]:
            numeros.insert(2, numero)
        else:
            numeros.insert(3, numero)

    print(msg, numeros.index(numero))

print(numeros)

print("\n", f"{' Fim do Programa ':-^50}")
