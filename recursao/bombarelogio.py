time_start = int(input())
time_recordP = int(input())

def bomba_relogio(time_start,time_recordP):
    if time_start >=6:
        print(f"Atenção faltam {time_start} segundos...")
        bomba_relogio(time_start - 1,time_recordP)
    else:
        if time_start > 1 and time_start != 5:
            print(f"Atenção faltam {time_start} segundos...")
            bomba_relogio(time_start - 1,time_recordP)
            
    if time_start==5:
        print("Seu tempo está acabando!")
        bomba_relogio(time_start - 1,time_recordP)
        #print('Seja rápido. Falta 1 segundo')
        #print("Cabum!!!! Explodiu")
  
  
if time_start==0:
    print("Cabum!!!! Explodiu")
    
else:
    bomba_relogio(time_start,time_recordP)
    
if time_start <= time_recordP and time_start!=0:
    print("Bomba desativada automaticamente!")
    
if time_start > time_recordP and time_start!=0:
    print('Seja rápido. Falta 1 segundo')
    print("Cabum!!!! Explodiu")
