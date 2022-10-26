# Objetivo: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# Data: 19/10/22
# Author: Washington

from random import sample
print("{:-^50}".format("Inicio do Programa"), "\n")

aluno1 = input("Entre com o nome do primeiro aluno: ")
aluno2 = input("Entre com o nome do segundo aluno: ")
aluno3 = input("Entre com o nome terceiro aluno: ")
aluno4 = input("Entre com o nome do quarto aluno: ")

print("A ordem de apresentação é :", sample([aluno1, aluno2, aluno3, aluno4], k=4))

print("\n", "{:-^50}".format("Fim do Programa"))