# Objetivo: Crie um programa que tenha função factorial() que receba 2 parâmetros:
# o primeiro indica o número a calcular e o segundo chamado show, que será um valor lógico opcional indicando se será
# mostrado ou não na tela o processo de cálculo do fatorial.
# Data: 14/11/22
# Author: Washington

print(f"{' Cálculo do Factorial ':-^50}", "\n")

def fatorial(valor, show=False):
    """Cálcula o fatorial de um núemro

    Args:
        valor (int): Número que se deseja o fatorial
        show (bool, optional): Mostra ou não o cálculo. Default to False.

    Returns:
        O fatorial do número valor
    """
    num = valor -1
    fat = valor
    calculo = str(valor)
    while num > 0:
        calculo += ' X ' + str(num)
        fat *= num
        num -= 1
    if show == True:
        return print(f"O fatorial de {valor} é {fat} : Cálculo ==> {calculo}")
    else:
        return print(f"O fatorial de {valor} é {fat}.")


fatorial(4, show=True)
print("-" * 50)
help(fatorial)

print("\n", f"{' Fim do Programa ':-^50}")