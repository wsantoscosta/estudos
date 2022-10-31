#Crie um programa que leia dois valores e mostre um menu na tela:
#1 -Somar 2 - Multiplicar 3 - Maior 4 - Novos números 5 - Sair

opcao = 0
print("{:-^40}".format(" Trabalhando com números "))

while opcao != 5:
    
    if opcao == 0:
        num1 = float(input("Entre com o primeiro número: "))
        num2 = float(input("Entre com o segundo número: "))

    print("{:-^40}".format(" Menu "))
    print("""
[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior 
[ 4 ] - Novos números
[ 5 ] - Sair 
""") 
    opcao = int(input("O que deseja fazer? "))

    if opcao < 1 or opcao > 5:
        print("Opção inválida! [1, 2, 3, 4 ou 5]")
    elif opcao == 1:
        resultado = num1 + num2
        print("A soma dos valores {:.2f} + {:.2f} = {:.2f}".format(num1, num2, resultado))
    elif opcao == 2:
        resultado = num1 * num2
        print("A soma dos valores {:.2f} x {:.2f} = {:.2f}".format(num1, num2, resultado))
    elif opcao == 3:
        if num1 > num2:
            resultado = num1
        if num1 < num2:
            resultado = num2
        else:
            resultado = num1
        print("O maior número é {:.2f}".format(resultado))
    if opcao == 4:
        print("{:-^40} \n".format(" Trabalhando com números "))
        opcao = 0