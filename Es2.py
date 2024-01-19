# esercizio 2
class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione

    def libro_recente(self):
        anno_corrente = 2024  # Puoi utilizzare una funzione per ottenere l'anno corrente effettivo
        return anno_corrente - self.anno_pubblicazione <= 10

# Esempio di utilizzo della classe Libro
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954)
print(f"Il libro è recente? {libro1.libro_recente()}")


