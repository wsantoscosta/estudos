# Objetivo: Faça um programa que tenha uma função chamada contador() que receba três parâmetros 
# inicio, fim e passo e realize a contagem: a) 1 a 10 , b) 10 a 0 c) Personalizada.
# Data: 11/11/22
# Author: Washington

print(f"{' Contar sequência ':-^50}", "\n")
def contador(inicio, fim, passo):
    n = inicio
    
    if passo == 0:
        passo = 1

    if inicio < fim:
        while n <= fim:
            print(f"{n} ", end="")
            n += abs(passo)
    if inicio > fim:
        while n >= fim:
            print(f"{n} ", end="")
            n -= abs(passo)
    print("\n")

contador(1, 10, 1)
contador(10,0,2)

print("-" * 50)
print("Agora é sua vez de personalizar a contagem.")

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))


print("-" * 50)  
print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
contador(inicio, fim, passo)

print("\n", f"{' Fim do Programa ':-^50}")