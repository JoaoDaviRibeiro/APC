def calcular_alcance_populacional(populacao_a, populacao_b, taxa_crescimento_a, taxa_crescimento_b):
    anos = 0

    while populacao_a <= populacao_b:
        populacao_a = int(populacao_a * (1 + taxa_crescimento_a/100))
        populacao_b = int(populacao_b * (1 + taxa_crescimento_b/100))
        anos += 1

        if anos > 1000:
            return "Mais de um milenio."

    return f"Vai alcancar em {anos} ano(s)."


populacao_a, populacao_b, taxa_crescimento_a, taxa_crescimento_b = map(float, input().split())
resultado = calcular_alcance_populacional(populacao_a, populacao_b, taxa_crescimento_a, taxa_crescimento_b)
print(resultado)
