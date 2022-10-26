# Objetivo: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escrever qual será a base para conversão. 
# 1 Binário, 2 - Octal e 3 - Hexadecimal.
# Data: 25/10/22
# Author: Washington

print("{:-^50}".format("Conversor de bases númericas."), "\n")

numero = int(input("Entre com um número inteiro : "))
base = int(input("""Converter para qual base ? 
1 - Binário
2 - Octal
3 - Hexadecimal
==> """))

if base == 1:
    print('O valor {}, convertido para binário é {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('O valor {}, convertido para octal é {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('O valor {}, convertido para hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print("Opção invalida! Entre com 1, 2 ou 3.")

print("\n", "{:-^50}".format("Fim do Programa"))