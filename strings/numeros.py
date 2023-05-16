count = 0

string = input()

for i in range(len(string)):
    if string[i] in '0123456789':
        count = count+1
    else:
        pass


print(count)
