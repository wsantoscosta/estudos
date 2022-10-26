# Objetivo: Crie um programa que leia a data de nascimento de sete pessoas. 
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores. > 21
# Data: 26/10/22
# Author: Washington
from datetime import date

print("{:-^50}".format(" Contar maioridade "), "\n")

maior = 0
menor = 0
ano_atual = date.today().year

for p in range(1, 8):
    ano = int(input("Informe a data de nascimento da {}ª pessoa: ".format(p)))
    if ano_atual - ano >= 21:
        maior += 1
    else:
        menor += 1

print("\nTotal de pessoas menores de idade : \033[32m{}\033[m.".format(menor))
print("Total de pessoas maiores de idade : \033[33m{}\033[m.".format(maior))

print("\n", "{:-^50}".format("Fim do Programa"))
