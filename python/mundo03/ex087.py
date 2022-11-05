# Objetivo: Aprimore o exercício anterior mostrando no final a soma de todos os pares, 
# a soma dos valores da terceira coluna , o maior valor da 2a linha.
# Data: 05/11/22
# Author: Washington

print(f"{' Criando uma matriz e somando elementos ':-^50}", "\n")

matriz = [[], [], []]
total_par = 0
total_col3 = 0
maior_valor_col2 = 0

for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(f"Entre com o {x} x {y} da matriz: "))
        matriz[x].insert(y, num)
        if num % 2 == 0:
            total_par += num
        if  y == 2:
            total_col3 += num
        if x == 1:
            if num > maior_valor_col2:
                maior_valor_col2 = num

print("-" * 50)

for m in range(0, 3):
    print(matriz[m])

print(f"O total dos números pares é: {total_par}.")
print(f"O total dos números da terceira coluna é: {total_col3}.")
print(f"O maior valor da linha 2 é: {maior_valor_col2}.")

print("\n", f"{' Fim do Programa ':-^50}")
