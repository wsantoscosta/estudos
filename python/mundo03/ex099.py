# Objetivo:Faça um programa que tenha uma função chamada maior() que receba vários parâmetros com valores
# inteiros, analisar os dados e mostrar o maior.
# Data: 11/11/22
# Author: Washington
from time import sleep

print(f"{' Testar maior valor ':-^50}", "\n")

def maior(*num):
    if len(num) > 0: 
        maior = num[0]
    else:
        maior = 0

    print("Números recebidos: ", end="")

    for n in num:
        print(n, end=" ", flush=True)
        sleep(1)
        if n > maior:
         maior = n

    print(f"\nForam informados {len(num)} valores.")
    print(f"O maior número informado foi {maior}.")
    print("-" * 50)


maior(10,8,15,33,45,3)
maior(1,2)
maior()
#maior(1,2,9,2)
#maior(2,4,7,9,33,12,109,45,25,55,77)
print("\n", f"{' Fim do Programa ':-^50}")