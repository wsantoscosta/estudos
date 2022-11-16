# Objetivo: Cria um código em Python que teste se o site pudim está acessível pelo computador usado.
# Data: 16/11/22
# Author: Washington

from urllib import request
print(f"{' Testar site ativo ':-^50}", "\n")

try:
   resp =request.urlopen("http://www.pudim.com.br")
except:
    print("Sorry. Website is no on-line.")
else:
    print("Yes. The web site is on-line.")
    #print(resp.read())

print("\n", f"{' Fim do Programa ':-^50}")