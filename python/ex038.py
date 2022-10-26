# Objetivo: Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem.
# O primeiro valor é maior , O segundo valor é maior ou não existe diferença.
# Data: 25/10/22
# Author: Washington

print("{:-^50}".format("Comparando dois números."), "\n")

num1 = int(input('Entre com o primeiro número: '))
num2 = int(input('Entre com o segundo número: '))

if num1 > num2:
    print('O maior número é {} e o menor é {}'.format('num1', 'num2'))
elif num2 > num1:
    print('O maior número é {} e o menor é {}'.format('num2', 'num1'))
else:
    print('Os número são iguais!')

print("\n", "{:-^50}".format("Fim do Programa"))
