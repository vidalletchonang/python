# Esercizio 10
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
indice = 0
somma = 0
while indice < len(guadagni):
    somma += guadagni[indice]
    indice += 1
print("Media: ", somma / len(guadagni))