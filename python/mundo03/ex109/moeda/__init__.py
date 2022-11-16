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