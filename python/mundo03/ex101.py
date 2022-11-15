# Objetivo: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se essa pessoa tem voto
# obrigatório, opcional ou negado.
# Data: 14/11/22
# Author: Washington



print(f"{' Situação do eleitor ':-^50}", "\n")

def voto():
    from datetime import date
    sit = ""
    ano_atual = date.today().year
    ano = int(input("Qual seu ano de nascimento: "))
    idade = ano_atual - ano

    if idade < 18 and idade >= 16 or idade >= 65:
        sit = "VOTO OPCIONAL"
    elif idade < 16:
        sit = "VOTO NEGADO"
    else:
        sit = "VOTO OBRIGATÓRIO"

    return print(f"Com {idade} anos: {sit}")


voto()

print("\n", f"{' Fim do Programa ':-^50}")
