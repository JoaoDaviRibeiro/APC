N = int(input())
P = int(input())

N >= 0
if N == 0:
    print("Cabum!!!! Explodiu")
elif N > P:
    for N in range(N, -1, -1):
    #for N in reversed(range(N + 1)):
        if N == 5:
            print("Seu tempo está acabando!")
        elif N > 1:
            print(f"Atenção faltam {N} segundos...")
        elif N == 1:
            print("Seja rápido. Falta 1 segundo")
        elif N == 0:
            print("Cabum!!!! Explodiu")
elif N <= P:
    for N in range(N, -1, -1):
        if N == 5:
            print("Seu tempo está acabando!")
        elif N > 1:
            print(f"Atenção, faltam {N} segundos...")
        elif N == 0:
            print("Bomba desativada automaticamente!")


    #if P > N:
     #   if N == 1:
      #      print("bomba desativada")
    #elif P <= N:
     #   if N == 1:
      #      print("Seja rápido, falta 1 segundo.")
       # elif N == 0:
        #    print("Cabum!")
