# Objetivo: A confederação de nacional de natação precisa de um programa que leia o ano de nascimento de
# um atleta e mostre sua categoria: até 9 mirim, até 14 infantil, até 19 júnior, até 25 sênior , acima master.
# Data: 25/10/22
# Author: Washington

from datetime import date

print("{:-^50}".format("Natação - Avaliação de categoria"), "\n")

ano_nascimento = int(input("Informe o seu ano de nascimento :"))
idade = date.today().year - ano_nascimento

if idade <= 9:
    print("A sua categoria com {} anos é \033[36m ==> Mirim \033[m.".format(idade))
elif idade <= 14:
    print("A sua categoria com {} anos é \033[32m ==> Infantil \033[m.".format(idade))
elif idade <= 19:
    print("A sua categoria com {} anos é \033[33m ==> Júnior \033[m.".format(idade))
elif idade <= 25:
    print("A sua categoria com {} anos é \033[31m ==> Sênior \033[m.".format(idade))
else:
    print("A sua categoria com {} anos é \033[35m ==> Master \033[m.".format(idade))

print("\n", "{:-^50}".format("Fim do Programa"))
