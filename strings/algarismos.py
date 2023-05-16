def substituir_numeros_por_algarismos(frase):
    numeros = {
        'zero': '0',
        'um': '1',
        'dois': '2',
        'três': '3',
        'quatro': '4',
        'cinco': '5',
        'seis': '6',
        'sete': '7',
        'oito': '8',
        'nove': '9'
    }

    frase_corrigida = ""
    contador_numeros = 0

    palavras = frase.split()

    for palavra in palavras:
        if palavra in numeros:
            frase_corrigida += numeros[palavra]
            contador_numeros += 1
        else:
            frase_corrigida += palavra
        frase_corrigida += " "

    return frase_corrigida.strip(), contador_numeros


frase = input()
frase_corrigida, contador_numeros = substituir_numeros_por_algarismos(frase)

print(frase_corrigida)

