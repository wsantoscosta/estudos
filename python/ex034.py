# Objetivo: Escreva um programa que leia o salário de um funcionário e calcule o aumento. > 1250 = 10%, < 15%.
# Data: 23/10/22
# Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

salario_atual = float(input("Entre com o salário atual do funcionário : R$  "))

if salario_atual > 1250.00:
    salario_novo = salario_atual + (salario_atual  *  10  /  100)
else:
    salario_novo = salario_atual + (salario_atual *  15  /  100)

print("O novo salário do funcionário é R$ {:.2f}".format(salario_novo))

print("\n", "{:-^50}".format("Fim do Programa"))