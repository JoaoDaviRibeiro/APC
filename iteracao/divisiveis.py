num = int(input())


for i in range(num + 1):
    if i % 3 == 0 and i % 7 == 0:
        print(i, end=" ")

