# Objetivo: Faça um programa que tenha uma função notas() que pode receber várias notas de aluno
# e vai retornar um dicionário com as requintes informações:
# qtde notas , maior nota, a menor nota, média da turma, situação (>7 boa, <>5 razoável e < 5
# péssima) adicione docstrings.
# Data: 14/11/22
# Author: Washington

print(f"{' Analisando notas do alunos ':-^50}", "\n")

def notas(* nota, sit = False):
    """Função que recebe notas de um aluno e analisa sua situação

    Args:
        *num : uma ou mais notas do aluno.
        sit (bool, optional): Mostrar ou não a situação. Default = False.

    Returns:
        Um Dic{}: Um dicionário com o total, a menor, a maior e a média das notas.
        Se Sit=True também retorna a situação. Boa, Razoável ou péssima
    """

    if len(nota) == 0:
        maior_nota = 0
        menor_nota = 0
    else:
        maior_nota = nota[0]
        menor_nota = nota[0]
    media = 0
    total = 0
    analise = {}

    for n in nota:
        total += n

        if n > maior_nota:
            maior_nota = n
        if n < menor_nota:
            menor_nota = n
    if len(nota) > 0:
        media = total / len(nota)
    else:
        media = 0
    
    analise["Total: "] = len(nota)
    analise["Maior: "] = maior_nota
    analise["Menor: "] = menor_nota
    analise["Media: "] = f"{media:.1f}"
    if sit == True:
        if media >= 7:
            analise["Situação: "] = "Boa"
        elif media < 7 and media >= 5:
            analise["Situação: "] = "Razoável"
        else:
            analise["Situação: "] = "Péssima"

    return analise



resp = notas(5,3,8, sit=True)
print(resp)
print("-" * 50)
help(notas)

print("\n", f"{' Fim do Programa ':-^50}")
