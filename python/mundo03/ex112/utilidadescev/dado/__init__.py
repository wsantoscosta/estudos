def leiadinheiro(msg):
    
    
    while True:
        
        
        num = str(input(msg)).replace(".", "")
        num = num.replace(",", ".")
        
        aux = num.replace(".", "")

        if aux.isnumeric():
            return float(num)
            break
        else:
            print("Erro: Informação não é numerica")
