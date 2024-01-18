# Esercizio 7
stringa = input("Inserisci una stringa: ")
while len(stringa) < 6:
    stringa *= 2
print(stringa, " => ", stringa[:3], '...', stringa[-3:])
