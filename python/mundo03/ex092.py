# Objetivo: Crie um programa que leia nome , ano de nascimento e ctps, cadastre-os (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de
# contratação e o salário. Calcule além da idade, com quantos anos a pessoa vai se aposentar.
# Data: 10/11/22
# Author: Washington

from datetime import date
print(f"{' Cadastro de Pessoas ':-^50}", "\n")

pessoas = {}

pessoas["nome"] = str(input("Entre com o nome: "))
ano_nascimento = int(input("Entre com o ano de nascimento: "))
pessoas["idade"] = date.today().year - ano_nascimento
pessoas["ctps"] = int(input("Entre com o número da CTPS - 0 se não tiver :"))

if pessoas["ctps"] > 0:
    pessoas["ano_contratacao"] = int(input("Entre com o ano de contratação: "))
    pessoas["salario"] = float(input("Entre com o salário: "))
    pessoas["idade_aposenta"] = (pessoas["ano_contratacao"] + 35) - ano_nascimento


print(f"{' Resumo ':-^50}")
for k, v in pessoas.items():
    print(f"{k} tem o valor: {v}")


print("\n", f"{' Fim do Programa ':-^50}")