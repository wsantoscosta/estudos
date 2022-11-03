# Objetivo: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista na lista ele não será adicionado. No final serão exibidos todos os valores únicos em ordem crescente.
# Data: 03/11/22
# Author: Washington

print(f"{' Preenchendo lista com números únicos ':-^50}", "\n")

valores = []

while True:
    continua = ' '

    valor = int(input("Digite um valor: "))
    if valor in valores:
        print("Valor já existe. Não será incluido!")
    else:
        valores.append(valor)
        print("Valor incluido com sucesso.")
    print("-" * 50)
    while continua not in 'SN':
        continua = str(input("Deseja continuar? [S/N] ")).strip().upper()
        
    if continua == "N":
        break

valores.sort()
print("-" * 50)
print(f"Os valores incluidos foram: {valores}.")

print("\n", f"{' Fim do Programa ':-^50}")