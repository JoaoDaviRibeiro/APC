print("O programa funciona?")
input1 = input()

if input1 == "SIM":
    print("Você entende o que fez?")
    input2 = input()
    if input2 == "SIM":
        print("Ótimo. Então não mexe!")
    elif input2 == "NÃO":
        print("Já foi na tutoria?")
        input3 = input()
        if input3 == "SIM":
            print("Choremos!")
        elif input3 == "NÃO":
            print("Temos um time a disposição!")

elif input1 == "NÃO":
    print("Você sabe onde está o erro?")
    input4 = input()
    if input4 == "NÃO":
        print("Já foi na tutoria?")
        input5 = input()
        if input5 == "SIM":
            print("Choremos!")
        elif input5 == "NÃO":
            print("Temos um time a disposição!")
    elif input4 == "SIM":
        print("Acha que pode solucionar sozinho?")
        input6 = input()
        if input6 == "SIM":
            print("Então mão na massa!")
        elif input6 == "NÃO":
            print("Já pesquisou no Google?")
            input7 = input()
            if input7 == "NÃO":
                 print("Corre lá então!")
            elif input7 == "SIM":
                 print("Já foi na tutoria?")
                 input8 = input()
                 if input8 == "SIM":
                    print("Choremos!")
                 elif input8 == "NÃO":
                    print("Temos um time a disposição!")
