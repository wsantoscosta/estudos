# Objetivo: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. 
# Caso esteja errado peça a digitação novamente até ter um valor válido.
# Data: 27/10/22
# Author: Washington

print("{:-^50}".format(" Teste de texto recebido [M/F] "), "\n")

sexo = "s"

while sexo not in "MF":

    sexo = str(input("Qual o seu gênero sexual [M - Masculino / F - Feminino.]: ")).strip().upper() [0]

    if  sexo != "M" and sexo != "F":
        print("Opção incorreta! - Digite M ou F.")
       

print("Gênero {} registrado com sucesso!".format(sexo))   
print("\n", "{:-^50}".format("Fim do Programa"))
