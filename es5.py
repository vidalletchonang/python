# Esercizio 5
n = int(input("Quante potenze vuoi calcolare? "))
x = 0
potenza = 1
while x <= n and potenza < 25000:
    print(2, "^", x, '=', 2**x)
    x += 1
    potenza = 2**x

