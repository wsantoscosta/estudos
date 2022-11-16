# Objetivo: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
# em um arquivo de texto simples. O sistema só vai ter 2 opções cadastrar uma nova pessoa e listar todas
# as pessoas cadastradas.
# Data: 16/11/22
# Author: Washington

print(f"{' Cadastro de pessoas em arquivo ':-^50}", "\n")

def menu():
    while True:
        print("-" * 40)
        print(f"{' Cadastro de pessoas ':^40}")
        print("-" * 40)
        print("""
1 - Incluir
2 - Listar
3 - Sair""")
        print("-" * 40)

        try:
            opcao = int((input("\033[32mOpção: \033[m")))
        except:
            print("\033[31mErro tipo de opção inválida\033[m")
            continue

        if opcao == 1:
            incluir()
        elif opcao == 2:
            listar("pessoas.txt")
        elif opcao == 3:
            print("Encerrando...")
            break
        else:
            print("\033[31mErro: Opção Inválida\033[m")
    

def incluir():
    print("-" * 40)
    print(f"{' Inclusão de Pessoas ':^40}")
    arq = open("pessoas.txt", "a")
    nome = str(input("Nome  : ")).strip()
    while True:
        idade = input("Idade :")
        if idade.isnumeric():
            idade = int(idade)
            break
        else:
            print("\033[31mValor inválido\033[m")

    registro = f"{nome:<15} {idade:>10}\n"
    arq.write(registro)
    arq.close()
    print("Registro incluido com sucesso.")


def listar(arquivo):
    try:
        arq = open(f"{arquivo}", "r")
    except:
        print("Arquivo Novo - sem registros.")
        arq = open(f"{arquivo}", "x")
        arq = open(f"{arquivo}", "r")
        
        
    print("-" * 40)
    print(f"{'Pessoas cadastradas':^40}")
    print("-" * 40)
    print(arq.read())
    arq.close()


menu()

print("\n", f"{' Fim do Programa ':-^50}")