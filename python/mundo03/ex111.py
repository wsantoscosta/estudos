# Objetivo: Crie um pacote chamado utilidadescev que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha
# tudo funcionando.
# Data: 15/11/22
# Author: Washington
from ex111.utilidadescev import moeda

print(f"{' Criando pacotes ':-^50}", "\n")
n = float(input("Digite o preço: R$ "))
moeda.resumo(n, 20, 10)


print("\n", f"{' Fim do Programa ':-^50}")