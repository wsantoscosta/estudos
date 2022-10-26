# Objetivo: Crie um programa que leia duas notas de um aluno e calcule a média, mostrando uma mensagem no
# final, de acordo com a média: < 5.0 reprovado, entre 5.0 e 6.9 em recuperação e > 7.0 aprovado.
# Data: 25/10/222
# Author: Washington

print("{:-^50}".format("Avaliação final de notas"), "\n")

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("\033[32mParabéns! Sua média final foi {:.1f} você está aprovado.\033[m".format(media))
elif media >= 5:
    print("\033[33mSua média final foi {:.1f}. Você está em recuperação.\033[m".format(media))
else:
    print("\033[31mSua média final foi {:.1f}. Você foi Reprovado.\033[m".format(media))

print("\n", "{:-^50}".format("Fim do Programa"))
