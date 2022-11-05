# Objetivo:Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final mostre um boletim contendo a média de cada aluno e permita que o usuário possa mostrar as notas de cada aluno individualmente.
# Data: 04/11/22
# Author: Washington

print(f"{' Cadastro de notas de alunos ':-^50}", "\n")
nota1 = []
nota2 = []
aluno = []
boletim = [aluno, nota1, nota2 ]

while True:
    continua = " "
    
    aluno.append(str(input("Entre com o nome do aluno: ")).strip().upper())
    nota1.append(float(input("Entre com a 1a nota: ")))
    nota2.append(float(input("Entre com a 2a nota: ")))

    while continua not in 'SN':
        continua = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    
    if continua == 'N':
        break

for i in range(0, len(aluno)):
    print(f"{i:^5}Nome: {aluno[i]:<12}\tMédia: {(nota1[i]+nota2[i])/2:2.1f}")
    print("-" * 50)

resposta = -1
while resposta != 999:
    print("-" * 50)
    resposta = int(input("Deseja ver as notas de qual aluno? 999 para sair.: "))
    
    if resposta == 999:
        break
    elif resposta < 0 or resposta > len(aluno) -1:
        print("Número inválido!!")
    else:
        print("-" * 50)
        print(f"Nome: {aluno[resposta]}\tNota1: {nota1[resposta]}\tNota2: {nota2[resposta]}")

print("\n", f"{' Fim do Programa ':-^50}")
