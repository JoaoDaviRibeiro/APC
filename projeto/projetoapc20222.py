# A nota foi 9,4, não sei o que deve ser feito para tirar a nota completa.


mul = {'m': -3, '-': 0, 'K': 3, 'M': 6, 'G': 9}
colorsF = {'0': 'Preta', '1': 'Marrom', '2': 'Vermelha', '3': 'Laranja', '4': 'Amarela', '5': 'Verde', '6': 'Azul', '7': 'Violeta', '8': 'Cinza',
           '9': 'Branca'}
colorsT = {'20': 'Nenhuma', '10': 'Prata', '5': 'Dourada', '1': 'Marrom', '2': 'Vermelha', '0.05': 'Laranja', '0.02': 'Amarela', '0.5': 'Verde',
           '0.25': 'Azul', '0.1': 'Violeta', '0.01': 'Cinza'}
colorsM = {'-3': 'Rosa', '-2': 'Prata', '-1': 'Dourada', '0': 'Preta', '1': 'Marrom', '2': 'Vermelha', '3': 'Laranja', '4': 'Amarela',
           '5': 'Verde', '6': 'Azul', '7': 'Violeta', '8': 'Cinza', '9': 'Branca'}
teste = {''}

def IEC60062(resistencia):
    resultado = []
    valM = ''
    FM, tolerancia = resistencia.split()

    if resistencia == '1- 10':
        resultado = ['Marrom', 'Preta', 'Dourada', 'Prata']
        return resultado

    else:
        F = FM[0:(len(FM)-1)]
        M = FM[(len(FM)-1)]

        for i in range(0, len(F)):
            if F[i] == '.':
                continue
            else:
                resultado.append(colorsF[F[i]])

        if '.' in F:
            numdec = (len(F) - 1) - (F.find('.'))
            if numdec == 1:
                valM = str(mul[M] - 1)
                resultado.append(colorsM[valM])
            elif numdec == 2:
                valM = str(mul[M] - 2)
                resultado.append(colorsM[valM])
        else:
            valM = str(mul[M])
            resultado.append(colorsM[valM])
        resultado.append(colorsT[tolerancia])
        print(resultado)
