# Objetivo: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No inicio pergunte o valor a ser sacado(inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# 50, 20, 10, 1
# Data: 31/10/22
# Author: Washington

print("{:-^50}".format(" Caixa Eletrônico "), "\n")

onca = macaco = arara = beija_flor = 0

valor = int(input("Qual valor deseja sacar: R$ "))

if valor > 50:
    onca = valor // 50
    resto = valor % 50
else:
    resto = valor

if resto  > 20:
    macaco = resto // 20
    resto = resto % 20

if resto  > 10:
    arara = resto // 10
    resto = resto % 10

if resto < 10:
    beija_flor = resto

print("Cédulas a receber : ")
print( f"R$ 50 ==> {onca}" ) 
print( f"R$ 20 ==> {macaco}")
print( f"R$ 10 ==> {arara}")
print( f"R$  1 ==> {beija_flor}")

print("\n", "{:-^50}".format("Fim do Programa"))
