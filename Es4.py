# esercizio 4
class ContoBancario:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def deposita(self, importo):
        self.saldo += importo
        print(f"Deposito effettuato. Nuovo saldo: {self.saldo}")

    def preleva(self, importo):
        if importo <= self.saldo:
            self.saldo -= importo
            print(f"Prelievo effettuato. Nuovo saldo: {self.saldo}")
        else:
            print("Saldo insufficiente per il prelievo.")

# Esempio di utilizzo della classe ContoBancario
conto = ContoBancario(1000)
conto.deposita(500)
conto.preleva(200)
