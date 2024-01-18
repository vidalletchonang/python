#Esercizio 11
prezzi = ["100 eur", "200 eur", "500 eur", "10 eur", "50 eur", "70 eur"]
indice = 0
while indice < len(prezzi):
    prezzi[indice] = prezzi[indice].replace("eur", "$")
    indice += 1
print(prezzi)

