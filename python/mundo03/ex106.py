# Objetivo: Faça um programa que utiliza o interactive help do python.
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra FIM o programa se encerrá. Use cores.
# Data: 14/11/22
# Author: Washington

print(f"{' Dicionário Interativo ':-^50}", "\n")

def cabecalho(texto):
    print("-" * (len(texto)-8))
    print(f"{texto}")
    print("-" * (len(texto)- 8))

def ajuda():
    
    while True:
    
        busca = str(input("Comando ou Função: ")).strip()
        
        if busca.upper() == "FIM":
            print("\nFinalizando...Boa Sorte.")
            break
        cabecalho(f"\033[42mAcessando o manual: {busca}\033[m")
                
        help(busca)
        print('-' * 30)
        


cabecalho("\033[46mSistema de ajuda do Pyhelp\033[m")
ajuda()


print("\n", f"{' Fim do Programa ':-^50}")