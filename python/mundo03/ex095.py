# Objetivo: Aprimore o desafio 93 para que funcione com vários jogadores incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
# Data: 09/11/22
# Author: Washington

print(f"{' Ficha jogador de futebol ':-^50}", "\n")

jogador = {}
jogadores = []
gols = []

while True:
    continua = ' '
    jogador.clear()
    gols.clear()

    jogador["nome"] = str(input("Nome: ")).strip()    
    jogador["partidas"] = int(input(f"Quantidade de jogos {jogador['nome']} jogou: "))

    if jogador["partidas"] > 0:
        for n in range(1, jogador["partidas"] + 1):
            gols.append(int(input(f"Gols feitos na partida {n}: ")))

    jogador["gols"] = gols[:]
    jogador["total_gols"] = sum(gols)
    
    jogadores.append(jogador.copy())

    print("-" * 50)

    while continua not in 'SN':
        continua = str(input("Deseja continuar [S/N] ?")).strip().upper()[0]
    if continua == 'N':
        break

print("-" * 50)

#print(jogadores)

print(f"{'Cod':^5}{'Nome':<10}{'Gols':<20}{'Total':^3} ")
for i, j in enumerate(jogadores):
    print(f"{i:^5}{j['nome']:<10}{str(j['gols']):<20}{j['total_gols']:^3}")

print("-" * 50)

resp = -1

while resp != 999:
    resp = int(input("Deseja ver dados de qual jogador (999- Sair): "))
    if resp == 999:
        break
    elif resp < 0 or resp > len(jogadores):
        print("Jogador não encontrado na relação.")
    else:
        print(f"Detalhamento do jogador : {jogadores[resp]['nome']}\n")
        for i,v  in enumerate(jogadores[resp]["gols"]):
            print(f"Na partida marcou {i} {v}gols")
    print("-" * 50, "\n")
print("\n", f"{' Fim do Programa ':-^50}")