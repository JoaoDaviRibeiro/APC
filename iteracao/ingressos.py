contador = 0

dinheirotot = 0

quantidade,preco = input().split(" ")
quantidade = int(quantidade)
preco = int(preco)


while True:
    contador = contador + 1

    if quantidade >= contador:
        dinheiro = int(input())
        dinheirotot += dinheiro

    else:

        media = int(dinheirotot/quantidade)
        if media < preco:
            print(f"media: {media}")
            print("rockeiros trabalhando ja")
            break
        else:
            print(f"media: {media}")
            print("o rock reinara mais uma vez")
            break
