m_sal = 0
contador = 0
while True:
    nome, salario = input().split(",")
    salario = float(salario)
    contador = contador + 1

    if nome != "Fim":
        if salario > m_sal:
            m_sal = salario
        elif salario <= m_sal:
            continue
    elif contador == 1:
        print("Não tem")
        break
    else:
        print(f"{m_sal:.2f}")
        break

