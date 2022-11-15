# Objetivo: Crie um programa que tenha a função lerint(), que vai funcionar de forma semelhante a função
# input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
# Data: 14/11/22
# Author: Washington
print(f"{' Valida valor recebido se Int ':-^50}", "\n")

def lerint(texto):

    while True:
        valor = input(texto)

        if valor.isnumeric():
            return valor
            break
        else:
            print("\033[31mERRO: Você não digitou um número.\033[m")


n = lerint("Digite um número: ")
print(f"Você digitou o número : {n}")

print("\n", f"{' Fim do Programa ':-^50}")