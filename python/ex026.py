# Objetivo: Faça um programa que leia uma frase e mostre:
# quantidade de letras "A", em que posição aparece pela 1ª vez e em que posição aparece pela última vez.
# Data: 21/10/22
# Author: Washington
print("{:-^50}".format("Inicio do Programa"), "\n")

frase = str(input("Entre com a frase: ")).strip().upper()
print("A frase digitado foi {}\nTem {} letras a.\nA primeira ocorrência está no posição {}\ne a úlima ocorrência está na posição {}"
      .format(frase, frase.count("A"), frase.find("A")+1, frase.rfind("A")+1))

print("\n", "{:-^50}".format("Fim do Programa"))
