# Objetivo: Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# Vai de alistar(indique quanto tempo), É hora de se alistar, Se já passou do tempo (indique quanto tempo.)
# Data: 25/10/22
# Author: Washington
from datetime import date 

print("{:-^50}".format("Avaliação para alistamento militar"), "\n")

ano_nascimento = int(input('Informe qual seu ano de nascimento: '))
idade = date.today().year - ano_nascimento

if idade == 18:
    print('Você está em período de alistamento militar! Não perca o prazo.')
elif idade > 18:
    print('Você já deveria ter se alistado a {} anos em {}'.format(idade - 18, ano_nascimento + 18))
else:
    print('Ainda falta {} anos que será em {} para você se alistar'.format(18 - idade, ano_nascimento + 18))

print("\n", "{:-^50}".format("Fim do Programa"))