# Objetivo: Escreva um programa para aprovar empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele deseja pagar. 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
# Data: 25/10/22
# Author: Washington

print("{:-^50}".format("Analisador de Empréstimo.."), "\n")

valor_casa = float(input("Informe o valor do imóvel : R$ "))
prazo_anos = int(input("Em quantos anos você deseja pagar : "))
salario_comprador = float(input("Informe o salário do comprador: R$ "))

print("-" * 50)

valor_prestacao = valor_casa / (prazo_anos * 12)
teto = salario_comprador * 30 /  100

print("O valor da prestação é  R$ {:.2f}".format(valor_prestacao))
print("O teto de 30% do salário é R$ {:.2f}".format(teto))

print("-" * 50)

if valor_prestacao > teto:
        print("O valor da prestacao excede o teto 30% do salário do comprador. \033[31m Empréstimo Negado. \033[m ")
else:
    print("\033[32mParabéns, o empréstimo foi aprovado. \033[m")

print("\n", "{:-^50}".format("Fim do Programa"))
