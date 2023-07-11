def recomenda(tags):
    freq = {}
    maximo = 0
    for lista in tags:
          for tag in lista:
              freq[tag] = freq.get(tag, 0) + 1
              maximo = max(maximo, freq[tag])
    resposta = []
    print(freq.items())
    for key, value in freq.items():
        if value == maximo:
            resposta.append(key)
    return resposta
