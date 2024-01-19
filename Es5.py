# esercizio 5
class Prodotto:
    def __init__(self, nome, prezzo, quantita_disponibile):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita_disponibile = quantita_disponibile

    def calcola_costo_totale(self, quantita):
        return self.prezzo * quantita

    def verifica_disponibilita(self, quantita_da_acquistare):
        return self.quantita_disponibile >= quantita_da_acquistare

# Esempio di utilizzo della classe Prodotto
prodotto1 = Prodotto("Smartphone", 500, 10)
costo_totale = prodotto1.calcola_costo_totale(3)
disponibile = prodotto1.verifica_disponibilita(5)

print(f"Costo totale: {costo_totale}")
print(f"Disponibile: {disponibile}")
