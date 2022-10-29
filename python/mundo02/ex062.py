# Objetivo: Melhore o desafio 61 perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programam encerra quando ele disser que quer 0 termos.
# Data: 27/10/22
# Author: Washington

print("{:-^50}".format("Início do Programa"), "\n")

primeiro_termo = int(input("Entre com o primeiro termo da PA: "))
razao = int(input("Entre com a razão da PA : "))
termo = 1
valor_termo = primeiro_termo
ultimo_termo = (primeiro_termo + (10 - 1) * razao)

while valor_termo <= ultimo_termo:
    print("O {:>2}º termo da PA : {:>3}".format(termo, valor_termo))
    valor_termo += razao
    termo += 1

    if valor_termo > ultimo_termo:
        continua = int(input("Deseja mais quantos termos ? Digite 0 para sair. "))
        if continua > 0:
            ultimo_termo += continua  * razao

print("\n", "{:-^50}".format("Fim do Programa"))
