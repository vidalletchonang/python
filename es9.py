# Esercizio 9
k = int(input("Quale numero? "))
n = int(input("Quante potenze? "))
p = n
potenze = []
while(n >= 0):
    potenze.append(k**n)
    n -= 1
potenze.sort()
print("Prime ", p, " potenze di ", k, " => ", potenze)
