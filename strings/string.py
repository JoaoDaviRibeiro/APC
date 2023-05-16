string = input()
nova = ''

for i in range(len(string)):
    if string[i] == '':
        pass
    else:
        if i%2 != 0 and string[i]!=' ':
            nova = nova + string[i]
        else:
            pass

  
print(nova)
