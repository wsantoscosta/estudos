# Objetivo: Faça um programa que lê o salário de um funcionário de calcula um aumento de N%.
# Data: 18/10/22
#Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

salario = float(input("Entr com o salário do funcionário: R$ "))
aumento_percentual = float(input("Entre com o percentual de aumento: % "))

aumento = salario * (aumento_percentual / 100)

print("O salário atual do funcionário é R$ {:.2f},o valor de aumento é R$ {:.2f} e o novo salário é R$ {:.2f}"
      .format(salario, aumento, salario + aumento), "\n")

print("{:-^50}".format("Fim do Programa"))