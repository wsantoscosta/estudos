# Objetivo: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final tudo isso será guardado em um dicionário incluindo o total de gols feitos durante
# o campeonato.
# Data: 10/11/22
# Author: Washington

print(f"{' Aproveitamento Jogador de Futebol ':-^50}", "\n")

jogador = {}
gols = []
jogador["nome"] = str(input("Nome: ")).strip()
jogador["partidas"] = int(input(f"Quantidade de jogos {jogador['nome']} jogou: "))

if jogador["partidas"] > 0:
    for n in range(1, jogador["partidas"] + 1):
        gols.append(int(input(f"Gols feitos na partida {n}: ")))

jogador["gols"] = gols[:]
jogador["total_gols"] = sum(gols)

print("-" * 50)

for k, v in jogador.items():
    print(f"{k:<15} = {v}")

print("-" * 50)

print(f"O jogador {jogador['nome']} fez {jogador['partidas']} partidas")

for k,v in enumerate(gols):
    print(f"==> Na {k+1}ª partida fez {v} gols. ")

print(f"Total de gols: {jogador['total_gols']}")

print("\n", f"{' Fim do Programa ':-^50}")