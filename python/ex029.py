# Objetivo: Escreva um programa que leia a velocidade de um carro. Escreva na tela se ele foi multada e o valor da multa.
# Acima de 80 km/h e multa de R$ 7,00 por km acima do limite.
# Data: 23/10/22
# Author: Washington
print("{:-^50}".format("Inicio do Programa"), "\n")

velocidade = float(input("Qual a velocidade do veículo? (km/h) "))

if velocidade > 80:
    print("Você ultrapassou o limite de velocidade de 80 km/h ==> + {}, e será multado em R$ {:.2f}".format(velocidade - 80,(velocidade - 80) * 7))
else:
    print("Continue assim. Boa viagem!!!")

print("\n", "{:-^50}".format("Fim do Programa"))
