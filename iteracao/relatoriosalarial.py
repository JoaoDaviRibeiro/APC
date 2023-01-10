max_sal = 0.00
min_sal = 0.00
nome_min_sal = ""
nome_max_sal = ""
contador = 1
salariotot = 0

n = int(input())
if n > 1:
    while contador <= n:
        nome, salario = input().split(",")
        salario = float(salario)
        salariotot += salario
        if contador == 1:
            min_sal = salario
            nome_min_sal = nome
            max_sal = salario
            nome_max_sal = nome
            contador = contador + 1
        else:
            contador = contador + 1
            if salario < min_sal:
                min_sal = salario
                nome_min_sal = nome

            elif salario > max_sal:
                max_sal = salario
                nome_max_sal = nome

    print(f"{salariotot / (n):.2f}")
    print(f"{nome_max_sal} {max_sal:.2f}")
    print(f"{nome_min_sal} {min_sal:.2f}")

elif n == 0:
    print("Não tem média")
    print("Não tem")
    print("Não tem")
else:
    nome, salario = input().split(",")
    salario = float(salario)
    nome_min_sal = nome
    nome_max_sal = nome
    min_sal = salario
    max_sal = salario
    print(f"{salario:.2f}")
    print(f"{nome_max_sal} {max_sal:.2f}")
    print(f"{nome_min_sal} {min_sal:.2f}")
