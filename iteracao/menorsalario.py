m_sal = 1000000000.00
nome_m_sal = ""
contador = 0

while True:
    nome, salario = input().split(",")
    salario = float(salario)
    contador = contador + 1

    if nome != "Fim":
        if salario < m_sal:
            m_sal = salario
            nome_m_sal = nome
        elif salario > m_sal:
            continue
    elif contador == 1:
        print("Não tem")
        break
    else:
        print(nome_m_sal)
        break

