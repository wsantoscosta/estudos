# Objetivo: 045 - Crie um programa que faça o computador jogar jokenpô com você
# Data: 25/10/22
# Author: Washington

from random import randint

print("{:-^50}".format("Jokenpô"), "\n")

escolha = int(input("1- Pedra, 2- Papel ou 3- Tesoura: "))
pc = randint(1, 3)

if pc == 1 and escolha ==1:
    print("Você escolheu Pedra e o PC escolheu {} - Pedra. EMPATE".format(pc))
elif pc == 1 and escolha == 2:
    print("Você escolheu Papel e o PC escolheu {} - Pedra. Você ganhou!".format(pc))
elif pc == 1 and escolha == 3:
    print("Você escolheu Tesoura e o PC escolheu {} - Pedra. Você perdeu!".format(pc))
elif pc == 2 and escolha == 2:
    print("Você escolheu Papel e o PC escolheu {} - Papel. Empate".format(pc))
elif pc == 2 and escolha == 1:
    print("Você escolheu Pedra e o PC escolheu {} - Papel. Você perdeu!".format(pc))
elif pc ==2 and escolha == 3:
    print("Você escolheu Tesoura e o PC escolheu {} - Papel. Você ganhou!".format(pc))
elif pc == 3 and escolha == 3:
    print("Você escolheu Tesoura e o PC escolheu {} - Tesoura. EMPATE!".format(pc))
elif pc == 3 and escolha == 1:
    print("Você escolheu Pedra e o PC escolheu {} - Tesoura. Você venceu!".format(pc))
else:
    print("Você escolheu Papel e o PC escolheu {} - Tesoura. Você perdeu!".format(pc))

print("\n", "{:-^50}".format("Fim do Programa"))