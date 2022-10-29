# Objetivo: Crie um programa que leia dois valores e mostre um menu na tela:
#  1 -Somar 2 - Multiplicar 3 - Maior 4 - Novos números 5 - Sair
# Data: 27/10/22
# Author: Washington

print("{:-^50}".format(" Calculadora "), "\n")

maior = ""
operacao = ""
opcao = 0

while opcao != 5:
    numero1 = float(input("Entre com o 1º número para o cálculo: "))
    numero2 = float(input("Entre com o 2º número para o cálculo: "))

    print("""
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Testar maior
    [ 4 ] Novos números
    [ 5 ] Sair
    ----------------------""")
    opcao = int(input("Entre com a opção desejada: "))
    
    if opcao == 5:
        break
    elif opcao == 4:
        continue
    elif opcao == 1:
        operacao = " + "
        resultado = numero1 + numero2
    elif opcao == 2:
        operacao = " x "
        resultado = numero1 * numero2
    elif opcao == 3:
        operacao = " teste maior "
        if numero1 > numero2:
            maior = "Número 1 é maior"
        elif numero1 < numero2:
            maior = "Número 2 é maior"
        else:
            maior = "O números são iguais."
    else: 
        print("\033[31mOpção inválida ! [1 , 2, 3, 4 ou 5]\033[m")
    
    if opcao != 3:
        print("\033[42mResultado :  {} {} {} : {}\033[m".format(numero1, operacao, numero2, resultado))
    else:
        print("\033[42mResultado :  {} {} {} : {}\033[m".format(numero1, operacao, numero2 , maior))

print("\n", "{:-^50}".format("Fim do Programa"))
