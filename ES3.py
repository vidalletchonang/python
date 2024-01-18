# esercizio 3
# Dizionario proprietario-auto
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"}

# Utilizza un ciclo for con il metodo .values() per stampare le auto che non sono una Multipla
print("Auto che non sono una Multipla:")
for auto in dizionario_auto.values():
    if auto != "Multipla":
        print(auto)
