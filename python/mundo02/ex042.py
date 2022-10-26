# Objetivo: Refaça o desafio 35 dos triângulos e, acrescentado o recurso de mostrar que tipo de triângulo será formado: 
# Equilátero, Isósceles ou Escaleno.
# Data: 25/10/22
# Author: Washington

print("{:-^50}".format("Avaliação de possíveis triângulos"), "\n")

reta1 = float(input("Ente com a medida da primeira reta: "))
reta2 = float(input("Entre com a medida da segunda reta: " ))
reta3 = float(input("Entre com a medida da terceira reta: "))

if (reta1 + reta2 > reta3) and (reta1 + reta3  > reta2) and (reta2 + reta3 > reta1):
    if reta1 == reta2 and reta1 == reta3:
        tipo = 'Equilátero'
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
    print('Pode ser formado um triângulo do tipo {}!'.format(tipo))
else:
    print('Não pode ser formado um triângulo')

print("\n", "{:-^50}".format("Fim do Programa"))