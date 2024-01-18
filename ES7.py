# esercizio 7
def media_numeri_maggiore_uguale_k(lista_numeri, K):
    # Filtra i numeri maggiori o uguali a K
    numeri_filtrati = [numero for numero in lista_numeri if numero >= K]

    # Verifica se ci sono numeri nella lista filtrata
    if not numeri_filtrati:
        return "Nessun numero maggiore o uguale a K nella lista."

    # Calcola la media dei numeri filtrati
    media = sum(numeri_filtrati) / len(numeri_filtrati)
    return media

# Esempio di utilizzo
lista_di_numeri = [3, 8, 5, 12, 7, 20]
K = 6

risultato = media_numeri_maggiore_uguale_k(lista_di_numeri, K)
print(f"La media dei numeri maggiori o uguali a {K} è: {risultato}")
