# esrcizio 8
# Richiedi all'utente di inserire un numero
numero = int(input("Inserisci un numero: "))

# Inizializza una lista per memorizzare i divisori
divisori = []

# Trova i divisori del numero
for i in range(2, numero + 1):
    while numero % i == 0:
        # Aggiungi il divisore alla lista
        divisori.append(i)
        # Riduci il numero dividendo per il divisore
        numero //= i

# Stampa la lista dei divisori
print("I divisori di", numero, "sono:", divisori)

