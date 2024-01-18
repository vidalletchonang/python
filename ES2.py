# esercizio 2
# Creazione del dizionario proprietario-auto
proprietari_auto = {
    'Ada': 'Punto',
    'Ben': 'Multipla',
    'Charlie': 'Golf',
    'Debbie': '107'
}

# Stampa del dizionario completo
print("Dizionario proprietario-auto:")
print(proprietari_auto)

# Stampa dell'auto associata a Debbie
auto_di_debbie = proprietari_auto.get('Debbie', 'Proprietario non trovato')
print("L'auto di Debbie è una:", auto_di_debbie)
