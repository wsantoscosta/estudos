# Objetivo: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar para cada palavra quais são suas vogais.
# Data: 01/11/22
# Author: Washington

print(f"{' Contando vogais ':-^50}", "\n")

palavras = ("Ultraman", "Ultraseven", "Sawamu", "Fantomas", "Spectroman", "Thundercats", "DethNote", "TenjouTenge")

for p in palavras:
    print(f"{p:<20}", end=" ")
    
    for v in p:
        if v in 'aeiuoAEIOU':
            print(f"{v:2}", end="")
    
    print( )

print("\n", f"{' Fim do Programa ':-^50}")
