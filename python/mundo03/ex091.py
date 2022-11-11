# Objetivo: Faça um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios,
# guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem sabendo 
# que o vencedor tirou o maior número no dado.
# Data: 10/11/22
# Author: Washington

print(f"{' Jogando dados ':-^50}", "\n")

from random import randint

partida = {"Jogador1": 0, "Jogador2": 0, "Jogador3": 0, "Jogador4": 0}
ranking = {}
# Simplificar colocando na definição do dicionário o randint para cada jogador eliminando o for abaixo.
for jogador in range(1, 5):
    partida[f"Jogador{jogador}"] = randint(1, 6)
    print(f"O Jogador{jogador} tirou ", partida[f"Jogador{jogador}"])

# Simplificar utilizando sorted() + itemgetter de operator eliminado o while abaixo
ordem = 6
while ordem > 0:
    for k, v in partida.items():
        if v == ordem:
           ranking[k] = v
    ordem -= 1

print(f"{' Ranking dos Jogadores ':-^50}")
pos = 1

for k, v in ranking.items():
    print(f"{pos}º Lugar: {k} com {v}")
    pos += 1
    
print("\n", f"{' Fim do Programa ':-^50}")
