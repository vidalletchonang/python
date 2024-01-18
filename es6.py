# Esercizio 6
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend",
         "Frontend", "Data Analyst", "Backend"]

nuovi_studenti = ["Grace", "Henry"]
nuovi_corsi = ["Frontend", "Cybersecurity"]
lunghezza = len(nuovi_studenti)
indice = 0
while indice < lunghezza:
    studente = nuovi_studenti[indice]
    corso = nuovi_corsi[indice]
    if studente not in studenti:
        studenti.append(studente)
    if studenti.index(studente) >= len(corsi):
        corsi.append(corso)
    indice += 1
if len(corsi) == len(studenti):
    print(corsi)
