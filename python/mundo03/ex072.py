# Objetivo: Crie um programa que tenha um tupla totalmente preenchida com a contagem por extenso de zero até 20.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.
# Data: 01/11/22
# Author: Washington

print(f"{' Imprimr por extenso ':-^50}", "\n")

extenso = ("Zero","Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", 
                     "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezesete", "Dezoito", "Dezenove", "Vinte")

while True:
    numero = int(input("Entre com um número entre 0 e 20: "))

    if numero >= 0 and numero <= 20:
        print(f" {numero} ==> {extenso[numero]}")
        break
    else:
        print("Número Inválido!!!")

print("\n", f"{' Fim do Programa ':-^50}")