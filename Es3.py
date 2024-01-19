#esercizio 3
import math

class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio

    def calcola_area(self):
        return math.pi * self.raggio**2

    def calcola_circonferenza(self):
        return 2 * math.pi * self.raggio

# Esempio di utilizzo della classe Cerchio
cerchio1 = Cerchio(5)
print(f"Area del cerchio: {cerchio1.calcola_area()}")
print(f"Circonferenza del cerchio: {cerchio1.calcola_circonferenza()}")

