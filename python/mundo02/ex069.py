# Objetivo: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada o programa devera perguntar se o usuário quer ou não continuar. 
# No fim mostre quantas pessoas > 18 anos , quantos homens, quantas mulheres < 20.
# Data: 31/10/22
# Author: Washington

print("{:-^50}".format(" Analisando pessoas... "), "\n")

total_homens = 0
total_maiores = 0
total_mulheres = 0

while True:
    continua = ""
    sexo =" "

    while sexo not in 'MF':
        sexo = str(input("Entre o sexo da pessoa [M/F]: ")).strip().upper() [0]

    idade = int(input("Entre com a idade da pessoa: "))
    if sexo == "M":
        total_homens += 1
    else:
        if idade < 20:
            total_mulheres += 1

    if idade > 18:
        total_maiores += 1

    while continua != "S" and continua != "N":
        continua = str(input("Deseja continuar [S/N]: ")).strip().upper() [0]

    if continua == "N":
        break
    
    print(f"{' Próxima ... ':-^50}")

print(f"{' Resumo ':-^50}")
print(f"O total de homens foi : {total_homens}")
print(f"O Total de pessoas maiores de 18 anos foi: {total_maiores}")
print(f"O total de mulheres menores 20 anos foi: {total_mulheres}")

print("\n", "{:-^50}".format("Fim do Programa"))