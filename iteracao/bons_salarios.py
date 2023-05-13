saltot = 0
counter = 0

while True:
    nome, salario = input().split(',')
    salario = float(salario)
    saltot = saltot + salario
    counter = counter + 1
    if nome == 'Fim':
        if saltot == 0.00:
            print(f'{saltot:.2f}')
            break
        else:
            counter = counter - 1
            print(f'{saltot/counter:.2f}')
            break
