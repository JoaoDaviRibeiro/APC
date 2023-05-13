def fibonacci(n):
    if n == 1:
        print(0)
    elif n >= 2:
        print(0, 1, end=" ")

        a, b = 0, 1

        for _ in range(2, n):
            next_term = a + b
            print(next_term, end=" ")
            a, b = b, next_term





