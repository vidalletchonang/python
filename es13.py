# Esercizio 13
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D",
            "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

selezionati = []
ricerca = "95"
indice = 0
while indice < len(lista_cf):
    if ricerca in lista_cf[indice]:
        selezionati.append(lista_cf[indice])
    indice += 1
print("Selezionati: ", selezionati)
