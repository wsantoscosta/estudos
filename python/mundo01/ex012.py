# Objetivo: Faça um programa que lê o preço de um produto e mostra seu novo preço com desconto de N%.
# Data: 18/10/22
# Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

preco_produto = float(input("Entre com o preço de produto: R$  "))
desconto_percentual = float(input("Entre com o percentual de desconto: "))

desconto = preco_produto * (desconto_percentual / 100)

print("O preço do produto é R$ {:.2f}, o desconto é de R$ {:.2f} e o valor a pagar é R$ {:.2f}".format(preco_produto, 
      desconto, preco_produto - desconto))

print("{:-^50}".format("Fim do Programa"))