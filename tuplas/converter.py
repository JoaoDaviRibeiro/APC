def convert(lista):
    dicionario = {}
    for chave, valor in lista:
        if chave in dicionario:
            dicionario[chave].append(valor)
        else:
            dicionario[chave] = [valor]
    return dicionario
