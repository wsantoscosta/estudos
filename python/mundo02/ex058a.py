# Versão GUanabara com dica para mais/menos

from random import randint

computador = randint(0, 10)

print("Olá, sou seu computador e 'Pensei' em um número entre 0 e 10.")
print("Você consegue adivinhar?")

acertou = False
tentativas = 0

while acertou == False: 
    palpite = int(input("Entre com seu palpite :"))
    tentativas += 1

    if palpite == computador:
        acertou = True
        print("\033[41mParabés você acertou!!\033[m")
    else:
        if palpite > computador:
            print("\033[43mMenos...fresco.\033[m")
        else:
            print("\033[43mMais...corno\033[m")
print("Você precisou de {} tentativas para acertar.".format(tentativas))