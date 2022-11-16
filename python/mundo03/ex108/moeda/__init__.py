def aumentar(valor, indice):
    valor = valor + (valor * indice / 100)
    return valor

def diminuir(valor, indice):
    valor = valor - (valor * indice / 100)
    return valor

def dobro(valor):
    return valor * 2

def metade(valor):
    return valor / 2

def moeda(valor):
    import locale
    locale.setlocale(locale.LC_NUMERIC,"pt_BR.utf8")
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

    return locale.currency(valor, grouping=True)