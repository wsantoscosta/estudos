# Objetivo:Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele anotou. O programa deverá ser capaz de mostrar a ficha do
# jogador, mesmo que algum dado não tenha sido informado.
# Data: 14/11/22
# Author: Washington

print(f"{' Ficha do Jogador de Futebol ':-^50}", "\n")

def jogador(nome = "<desconhecido>", gols = 0):

    nome = str(input("Entre com o nome do jogador: "))
    if nome == "":
        nome = "<desconhecido>"
    gols = str(input("Entre com o numero de gols marcados: "))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    print(f"O jogador {nome} fez {gols} gols no campeonato.")


jogador()

print("\n", f"{' Fim do Programa ':-^50}")
