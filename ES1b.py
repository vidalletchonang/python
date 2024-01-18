# esercizio 1.b
# Calcolare e stampare tutte le prime 10 potenze di 2 utilizzando un ciclo for
potenze_di_due = []

for esponente in range(10):
    risultato = 2 ** esponente
    potenze_di_due.append(risultato)

print("Le prime 10 potenze di 2 sono:", potenze_di_due)
