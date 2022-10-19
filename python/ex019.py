# Objetivo: Um professor quer sortear um dos seus quatro alunos para apagar ao quadro. Faça um programa
# que avise ele, lendo os nomes e escrevendo o escolhido.
# Data: 19/10/22
# Author: Washington

from random import choice
print("{:-^50}".format("Inicio do Programa"), "\n")

aluno1 = input("Entre com o nome do primeiro aluno: ")
aluno2 = input("Entre com o nome do segundo aluno: ")
aluno3 = input("Entre com o nome do terceiro aluno: ")
aluno4 = input("Entre com o nome do quarto aluno: ")

print("O aluno sorteado foi ", choice([aluno1, aluno2, aluno3, aluno4]))

print("\n", "{:-^50}".format("Fim do Programa"))