# Esercizi 14
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
         "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

indice = 0
while indice < len(edizioni):
    if edizioni[indice] == 1:
        print(studenti[indice], corsi[indice])
    indice += 1