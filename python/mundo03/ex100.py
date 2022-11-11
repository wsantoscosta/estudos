# Objetivo: Faça um programa que tenha uma lista chamada números e duas funções chamadas 
# sorteio() e somapar(). A primeira função vai sortear números e vai coloca-los dentro da lista e a segunda
# função vai mostrar a soma entre todos os valores pares sorteados pela função.
# Data: 11/11/22
# Author: Washington
print(f"{' Criando funções sorteio e somapar ':-^50}", "\n")
from random import randint
from time import sleep

def sorteio(lst):
    print("Sorteando 5 numeros: ", end= "")
    for n in range(0, 5):
        numero = randint(1, 10)
        lst.append(numero)
        print(f"{numero}", end=" ", flush=True)
        sleep(1)
    print("\n\n>>>>> Fim do Sorteio <<<<<\n")

def somaPar(lst):
    total = 0
    for n in lst:
        if n % 2 == 0:
            total += n
    
    print(f"A soma dos pares de {lst} é {total}.")


lista = []
sorteio(lista)
somaPar(lista)


print("\n", f"{' Fim do Programa ':-^50}")