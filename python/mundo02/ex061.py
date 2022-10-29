# Objetivo: Refaça o desafio 51 lendo o primeiro termo e a razão de um PA mostrando os 10 primeiros termos
# da progressão usando a estrutura WHILE.
# Data: 27/10/22
# Author: Washington

print("{:-^50}".format(" Cálculo da PA com while "), "\n")

primeiro_termo = int(input("Entre com o primeiro termo da PA: "))
razao = int(input("Entre com a razão da PA : "))
termo = 1
valor_termo = primeiro_termo
ultimo_termo = (primeiro_termo + (10 - 1) * razao)

while valor_termo <= ultimo_termo:
    print("O {:>2}º termo da PA : {:>3}".format(termo, valor_termo))
    valor_termo += razao
    termo += 1

print("\n", "{:-^50}".format("Fim do Programa"))