# Objetivo: Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço e  condição de pagamento.
# A vista dn/ch 10% desconto, A vista cartão 5%, 2x cartão preço normal, > 3x cartão 20% juros.
# Data: 25/10/22
# Author: Washington

print("{:-^50}".format("Cálculo do valor a pagar"), "\n")


preco= float(input("Qual o preço do produto : R$ "))
forma_pgto = int(input("Qual a forma de pagamento? 1- Dinheiro, 2- Cartao débito, 3 - 2x , 4 - 3x ou mais: "))

if forma_pgto == 1:
    preco = preco - (preco * 10 / 100)
elif forma_pgto == 2:
    preco = preco - (preco * 5 / 100)
elif forma_pgto == 4:
    preco = preco + (preco * 0.20)

print("O preço a pagar na forma de pagamento {} é R$ {:.2f}".format(forma_pgto, preco))

print("\n", "{:-^50}".format("Fim do Programa"))