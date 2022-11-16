def aumentar(valor, indice, formata=False):
    valor = valor + (valor * indice / 100)
    if formata:
        return moeda(valor)
    else:
        return valor

def diminuir(valor, indice, formata=False):
    valor = valor - (valor * indice / 100)
    if formata:
        return moeda(valor)
    else:
        return valor

def dobro(valor, formata=False):
    if formata:
        return moeda(valor * 2)
    else:
        return valor * 2



def metade(valor, formata=False):
    if formata:
        return moeda(valor / 2)
    else:
        return valor /2 

        
def moeda(valor):
    import locale
    locale.setlocale(locale.LC_NUMERIC,"pt_BR.utf8")
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

    return locale.currency(valor, grouping=True)

def resumo(valor, aumento, desconto):
    print("-" * 37)
    print(f"{'Resumo':^37}")
    print("-" * 37)
    print(f"{'Preço analisado:':<20} {valor:>15}")
    print(f"{'Dobro do preço:':<20} {dobro(valor, True):>15}")
    print(f"{'Metade do preço:':<20} {metade(valor, True):>15}")
    print(f"{aumento}{'% de aumento:':<18} {aumentar(valor, aumento, True):>15}")
    print(f"{desconto}{'% de desconto:':<18} {diminuir(valor, desconto, True):>15}")
    print("-" * 37)