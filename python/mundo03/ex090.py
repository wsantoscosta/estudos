# Objetivo:Faça um programa que leia nome e média de um aluno guardando também a situação em um
# dicionário. No final mostre o conteúdo da estrutura na tela.
# Data: 10/11/22
# Author: Washington

print(f"{' gravando dados em um dicionário ':-^50}", "\n")

aluno = {"nome":"", "media":0.0, "situacao":""}

aluno["nome"] = str(input("Entre com o nome do aluno: "))
aluno["media"] = float(input(f"Entre com a média do {aluno['nome']}: "))
if aluno["media"] >= 7: 
    aluno["situacao"] = "Aprovado"
elif aluno["media"] >= 5:
    aluno["situacao"] = "Recuperação"
else:
    aluno["situacao"] = "Reprovado"

for key, value in aluno.items():
    print(f"{key.capitalize()} é igual a {value}")

print("\n", f"{' Fim do Programa ':-^50}")
