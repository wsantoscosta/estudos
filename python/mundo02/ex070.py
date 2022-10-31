# Objetivo: Crie um programa que leia o nome e o preço de vários produtos.
#  O programa deverá perguntar se o usuário quer continuar.
#  No final mostrar Total da compra, Qtde de produtos > 1000, produto mais barato.
# Data: 31/10/22
# Author: Washington

print("{:-^50}".format(" Lista de Compras "), "\n")

total_compra = 0
produto_maior_1000 = 0
produto_mais_barato = ""
menor = 0


while True:
    continua = " "
    produto = str(input("Entre com o nome do produto: "))
    preco = float(input("Entre com o preço do produto: R$ "))

    if total_compra == 0:
        total_compra = preco
        #produto_mais_barato = produto
        #menor = preco
    else:
        total_compra += preco
    
    if preco > 1000:
        produto_maior_1000 += 1
    
    if preco < menor  or menor == 0:
        produto_mais_barato = produto
        menor = preco

    while continua != "S" and continua != "N":
        continua = str(input("Deseja continuar? [S/N] ")).strip().upper() [0]

    if continua == "N":
        break

print(f"{' Resumo':-^50}")
print(f"Total da compra: R$ {total_compra:.2f}.")
print(f"Produto mais barato ==> {produto_mais_barato} = {menor:.2f}.")
print(f"Produtos maiores que R$ 1.000,00 ==> {produto_maior_1000}.")

print("\n", "{:-^50}".format("Fim do Programa"))
