# esercizio 6
def tre_numeri_piu_grandi(lista_numeri):
    # Verifica se la lista ha almeno tre elementi
    if len(lista_numeri) < 3:
        return "La lista deve contenere almeno tre numeri."

    # Ordina la lista in ordine decrescente
    lista_numeri_ordinata = sorted(lista_numeri, reverse=True)

    # Restituisci i primi tre numeri ordinati (possono essere uguali)
    return lista_numeri_ordinata[:3]

# Esempio di utilizzo
lista_di_numeri = [5, 10, 8, 15, 8, 12, 18, 20]
risultato = tre_numeri_piu_grandi(lista_di_numeri)

print(f"I tre numeri più grandi sono: {risultato}")
