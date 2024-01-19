# esercizio 6
class AnalisiDati:
    def __init__(self, dati):
        self.dati = dati

    def calcola_media(self):
        return sum(self.dati) / len(self.dati) if self.dati else None

    def calcola_varianza(self):
        media = self.calcola_media()
        return sum((x - media) ** 2 for x in self.dati) / len(self.dati) if self.dati else None

# Esempio di utilizzo della classe AnalisiDati
dati_numerici = [10, 15, 20, 25, 30]
analisi = AnalisiDati(dati_numerici)

media = analisi.calcola_media()
varianza = analisi.calcola_varianza()

print(f"Media: {media}")
print(f"Varianza: {varianza}")
