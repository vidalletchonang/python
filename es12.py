# Esercizio 12
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma",
            "Faith", "Grace", "Henry", "Isabelle", "John"]
squadra_1 = []
squadra_2 = []
indice = 0
while indice < len(studenti):
    if indice % 2 == 0:
        squadra_1.append(studenti[indice])
    else:
        squadra_2.append(studenti[indice])
    indice += 1
print("Squadra 1: ", squadra_1)
print("Squadra 2: ", squadra_2)
