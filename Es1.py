# esercizio 1
class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def stampa_informazioni(self):
        print(f"Nome: {self.nome}, Cognome: {self.cognome}, Età: {self.eta}")

# Esempio di utilizzo della classe Persona
persona1 = Persona("Alice", "Rossi", 30)
persona1.stampa_informazioni()

