# Objetivo: Programa que lê a largura e altura de uma parede em metros, calcula sua área e a quantidade de tinta necessária para pinta-la,
#           sabendo que cada litro de tinta pinta uma área de 2m.
# Data: 18/10/22
#Author: Washington

print("{:-^50}".format("Inicio do Programa"), "\n")

largura = float(input("Entre com a largura da parede em metros: "))
altura = float(input("Entre com a altura da parede em metros: "))

area_da_parede = largura * altura

quantidade_de_tinta = area_da_parede / 2

print("A parede tem uma área de {}m² - metros quadrados.".format(area_da_parede))
print("Para pinta-lá será necessário {} litros de tinta".format(quantidade_de_tinta))

print("{:-^50}".format("Fim do Programa"))