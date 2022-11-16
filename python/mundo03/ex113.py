# Objetivo: Reescreva a função leiaint() que fizemos no exercício 104 incluindo agora a possibilidade de
# digitação de um número de tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma
# funcionalidade.
# Data: 16/11/22
# Author: Washington

print(f"{' Utilizando captura de exceçẽs ':-^50}", "\n")
def leiaint(texto):

    while True:
        try:
            valor = int(input(texto))
        except KeyboardInterrupt:
            print("\033[34mUsuário escolheu não digitar.\033[m")
            return 0
            break
        except:
            print("\033[31mERRO: Você não digitou um número inteiro.\033[m")
        else:
            return valor
            break

def leiafloat(texto):

    while True:
        try:
            valor = float(input(texto))
        except KeyboardInterrupt:
            print("\033[34mUsuário escolheu não digitar.\033[m")
            return 0
            break
        except:
            print("\033[31mERRO: Você não digitou um número real.\033[m")
        else:
            return valor
            break
       
num1 = leiaint("Digite um número inteiro: ")
num2 = leiafloat("Digite um número real: ")
print(f"O valor inteiro digitado foi {num1} e o valor real foi {num2:.2f}")

print("\n", f"{' Fim do Programa ':-^50}")
