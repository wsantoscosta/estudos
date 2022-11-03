# Objetivo: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão está com parênteses abertos e fechado na ordem correta.
# Data: 02/11/22
# Author: Washington

print(f"{' Analisando expressões ':-^50}", "\n")

expressao = str(input("Entre com uma expressão com parênteses: ")).strip().upper()
somente_parenteses = ""
# Extrair '(' e ')' da expressao
for w in expressao:
    if w in "()":
        somente_parenteses += w

print(somente_parenteses, "\n")

meio = int(len(somente_parenteses) / 2)
abre = 0
fecha = 0
# Soma os indices de abre e fecha parenteses
for x, y  in enumerate(somente_parenteses):
    if y == "(":
        abre += x
    else:
        fecha += x

if fecha < abre or somente_parenteses[0] == ")" or somente_parenteses[-1] == "(" or len(somente_parenteses) % 2 != 0 or (fecha - abre) < meio:
    print("\033[31mExpressão inválida!!!\033[m")
else:
    print("\033[32mExpressão Válida!!!\033[m")

print("\n", f"{' Fim do Programa ':-^50}")
