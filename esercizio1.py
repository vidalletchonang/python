print("Hello")
# esercizio1.py

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
import timeit

def calcola_quadrato(numero):
    """
    Calcola il quadrato di un numero.

    Parameters:
    - numero (float o int): Il numero di cui calcolare il quadrato.

    Returns:
    - float o int: Il quadrato del numero.
    """
    return numero ** 2

# Misura il tempo di esecuzione della funzione per il valore 5
tempo_medio = timeit.timeit(lambda: calcola_quadrato(5), number=100000)

print(f"Tempo medio di esecuzione: {tempo_medio} secondi")

