indiceReclamacao = int(input())
percentReclamResolPrim = int(input())
percentCliCancel = int(input())
indiceIndisponibilidade = int(input())
canceladoPorProblema = int(input())

if (percentReclamResolPrim >= 60 and percentReclamResolPrim <=100):
    indice = indiceReclamacao - 5
elif percentReclamResolPrim > 100:
    indice = indiceReclamacao + 100
else:
    indice = indiceReclamacao + 15
print(f'{indice}')

if ( percentCliCancel >=10):
    if (canceladoPorProblema==1):
        indice = indice + 80
    else:
        indice = indice - 30
elif percentCliCancel < 10:
    if (canceladoPorProblema==1):
        indice = indice + 50
    else:
        indice = indice - 10
print(f'{indice}');

if (indiceIndisponibilidade >= 10):
    indice = indice + 70
else:
    indice = indice - 20
print(f'{indice}')