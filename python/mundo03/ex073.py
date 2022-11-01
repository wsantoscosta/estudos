# Objetivo: Crie uma tupla preenchida com os vinte primeiros colocados do campeonato brasileiro na ordem
# de colocação, depois mostre os 5 primeiros , os 4 últimos, em ordem alfabética e a posição da Chape (Botafogo).
# Data: 01/11/22
# Author: Washington

print(f"{' Times do Brasileirão 2022 ':-^50}", "\n")

times = ("Palmeiras", "Internacional" ,"Flamengo", "Fluminense", "Corinthians", "Athletico-PR", "Atlético-MG", "São Paulo", "Fortaleza",
"Botafogo", "América-MG", "Santos", "Goiás", "Bragantino", "Coritiba", "Cuiabá", "Ceará", "Atlético-GO", "Avaí", "Juventude")

print(times)
print(f"{' Em ordem alfabética':-^50}", "\n")
print(sorted(times))
print(f"{' 5 primeiros colocados ':-^50}", "\n")
print(times[0:5])
print(f"{' 4 Últimos colocados ':-^50}", "\n")
print(times[-4:])
print(f"{' Posição do Botafogo ':-^50}", "\n")
print(times.index("Botafogo") + 1,"º colocado")

print("\n", f"{' Fim do Programa ':-^50}")
