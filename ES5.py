# esercizio 5
def trova_minimo_massimo(lista_numeri):
    # Verifica se la lista è vuota
    if not lista_numeri:
        return None, None  # Restituisce None per entrambi minimo e massimo se la lista è vuota

    # Inizializza minimo e massimo con il primo elemento della lista
    minimo = massimo = lista_numeri[0]

    # Trova minimo e massimo iterando attraverso gli elementi della lista
    for numero in lista_numeri:
        if numero < minimo:
            minimo = numero
        elif numero > massimo:
            massimo = numero

    return minimo, massimo

# Esempio di utilizzo
lista_di_numeri = [4, 7, 1, 9, 3, 5, 8]
minimo, massimo = trova_minimo_massimo(lista_di_numeri)

print(f"Minimo: {minimo}, Massimo: {massimo}")
