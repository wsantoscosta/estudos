# \033[style;text;backgroundm
# style
#          0 = normal
#          1  = bold
#          5 = underline
#          7 = negativo(inverter)

#    texto        cor                 background
#       30          white               40
#       31          red                     41
#       32          green               42
#       33          yellow             43
#       34          blue                 44
#       35          magenta        45
#       36          cyano              46
#       37          grey                 47

print("Exemplo : \033[0;33;41m texto normal amarelo com fundo vermelho. \033[m")
print("Exemplo : \033[0;33;42m texto normal amarelo com fundo verde. \033[m")
print("Exemplo : \033[0;33;44m texto normal amarelo com fundo azul. \033[m")
