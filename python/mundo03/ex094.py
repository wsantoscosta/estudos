# Objetivo: Crie um programa que leia nome, sexo e idade de várias pessoas guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final mostre: qtde de pessoas, a
# média de idade, lista de mulheres e pessoas com idade acima da média.
# Data: 10/11/22
# Author: Washington

print(f"{' Gravando pessoas em listas e dicionários ':-^50}", "\n")

pessoa = {"nome": "", "sexo": "", "idade": 0}
cadastro = []
total_idade = 0

while True:
    continua = " "
    genero = " "
    
    pessoa["nome"] = str(input("Entre com o nome: ")).strip().capitalize()
    
    while genero not in 'MF':

        genero = str(input("Entre com o sexo [M/F]: ")).strip().upper()[0]
    
    pessoa["sexo"] = genero
    pessoa["idade"] = int(input("Entre com a idade: "))
    total_idade += pessoa["idade"]

    cadastro.append(pessoa.copy())

    while continua not in 'SN':

        continua = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    
    if continua == "N":
        break

print(f"{' Resumo ':-^50}")
print(f"O grupo tem {len(cadastro)} pessoas.")
media_idade = total_idade / len(cadastro)
print(f"A média de idade é {media_idade:.1f}")
print("As mulheres cadastradas foram: ", end="")
for pessoa in cadastro:
    if pessoa["sexo"] == "F":
        print(f"{pessoa['nome']}", end=" ")

print()
print("-" * 50)
print("\nLista de pessoas que estão acima da média: ")
print("-" * 50)
for pessoa in cadastro:
    if pessoa['idade'] > media_idade:
        print(f"Nome : {pessoa['nome']:<12} Sexo: {pessoa['sexo']:^3} Idade:{pessoa['idade']:>5}")

print("\n", f"{' Fim do Programa ':-^50}")