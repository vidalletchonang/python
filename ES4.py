# esercizio 4
# Dizionario originale proprietario-auto
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"}

# Nuovi dati dei proprietari-auto
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

# Aggiorna il dizionario_auto con i dati contenuti in nuovi_proprietari
dizionario_auto.update(nuovi_proprietari)

# Stampa il dizionario aggiornato
print("Dizionario proprietario-auto aggiornato:")
print(dizionario_auto)

# Stampa cosa è successo a Ben
print("Ben ora possiede un:", dizionario_auto.get("Ben"))
