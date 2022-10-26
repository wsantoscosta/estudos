# Objetivo: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e
# que se encontram no intervalo de 1 até 500.
# Data: 26/10/22
# Author: Washington

print("{:-^50}".format("Somando números ímpares múltiplos de 3"), "\n")

soma = 0
total  = 0

# for i in range(1, 501, 2) menos loops e sem checar os números pares
for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
        total += 1
print('Entre 1 e 500 a soma dos {} números ímpares múltiplos de 3 é {}'.format(total, soma))

print("\n", "{:-^50}".format("Fim do Programa"))