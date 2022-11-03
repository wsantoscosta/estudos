exp = str(input("Entre com uma expressão: "))
pilha = []

for simbolo in exp:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simbolo)
            break
if len(pilha) == 0:
    print("\033[34mExpressão válida!\033[m")
else:
    print("\033[31mExpressão Inválida!\033[m")
