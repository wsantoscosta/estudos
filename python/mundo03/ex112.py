# Objetivo: Dentro do pacote utilidadescev que criamos no desafio 111 temos um módulo chamado dado.
# Crie uma função chamada leiadinheiro() que seja capaz de funcionar como a função input(), mas com uma
# validação de dados para aceitar apenas valores que sejam monetários.
# Data: 15/11/22
# Author: Washington
from ex112.utilidadescev import dado
from ex112.utilidadescev import moeda

print(f"{' Teste com módulo de validação ':-^50}", "\n")

p = dado.leiadinheiro("Entre com um valor: R$ ")
moeda.resumo(p, 50, 30)

print("\n", f"{' Fim do Programa ':-^50}")
