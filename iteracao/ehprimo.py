def ehPrimo(x):
    if x < 2:
        return 0

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return 0

    return 1


def divisoresPrimos(x):
    count = 0
    if ehPrimo(x) == 1:
        return 0
    else:
        for i in range(1, x + 1):
            if x % i == 0 and ehPrimo(i):
                count += 1

    return count



