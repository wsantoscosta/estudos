# Objetivo: Adicione ao módulo moeda.py criado nos desafios anteriores uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado.
# Data: 15/11/22
# Author: Washington
from ex110 import moeda

print(f"{' Módulos e funções - resumo()':-^50}", "\n")

numero = float(input("Entre com o preço: "))
moeda.resumo(numero, 30, 15)


print("\n", f"{' Fim do Programa ':-^50}")
