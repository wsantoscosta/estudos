#Mostrar informações do dado recebido

dado = input("Entre com um dado: ")

print("O dado informado é do tipo: ", type(dado))

print ("O dado é alfanúmeiro? ", dado.isalnum())
print ("O dado é alfabético? ", dado.isalpha())
print("O dado é decimal? ", dado.isdecimal())
print("O dado esta em caixa alta? ", dado.isupper())
print("O dado esta em caixa baixa? ", dado.islower())
print("O dado é um título? ", dado.istitle())
print("O dado é numerico? ", dado.isnumeric())
