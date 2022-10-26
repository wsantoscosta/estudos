# Objetivo: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa mostre:
#   Média de idade do grupo
#   Qual é o nome do homem mais velho.
#   Quantas mulheres tem menos de 20 anos.
# Data: 26/10/22
# Author: Washington

print("{:-^50}".format(" Analisando grupo de pessoas "), "\n")

mais_velho = "-----"
idade_mais_velho = 0
mulheres_menores = 0
total_idade = 0

for i in range(1, 5):
    nome = str(input("Informe o nome da {} pessoa :  ".format(i))).strip().upper()
    idade = int(input("Informe a idade : "))
    sexo = str(input("Informe gênero sexual(M, F): ")).upper()
    
    if i == 1:
        if sexo == "M":
            mais_velho = nome
            idade_mais_velho = idade
        else:
            if idade < 20:
                mulheres_menores += 1
    if sexo == "M":
        if idade > idade_mais_velho:
            mais_velho = nome
            idade_mais_velho = idade
    else:
        if idade < 20:
            mulheres_menores += 1
    total_idade += idade
    print("-" * 50)
print("A média de idade do grupo é {:.1f}".format(total_idade / 4))
print("O nome do homem mais velho é {}".format(mais_velho))
print("Total de mulheres menores de 20 anos: {}".format(mulheres_menores))

print("\n", "{:-^50}".format("Fim do Programa"))