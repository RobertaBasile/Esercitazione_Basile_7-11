class Aggregazione:
    def __init__(self):
        self.numeri = []

    def aggiungi_numeri(self):
        self.numeri = []
        for i in range(5):
            numero = float(input(f"Inserisci il numero {i+1}: "))
            self.numeri.append(numero)

    def get_numeri(self):
        return self.numeri

class Confronto:
    def somma_posizioni(self, agg1, agg2):
        risultati = []
        for i in range(5):
            risultati.append(agg1.get_numeri()[i] + agg2.get_numeri()[i])
        return risultati

def main():
    while True:
        print("Valorizza la prima lista di 5 numeri:")
        agg1 = Aggregazione()
        agg1.aggiungi_numeri()

        print("Valorizza la seconda lista di 5 numeri:")
        agg2 = Aggregazione()
        agg2.aggiungi_numeri()

        confronto = Confronto()
        risultati = confronto.somma_posizioni(agg1, agg2)

        print("Risultati della somma delle posizioni corrispondenti:")
        for i, risultato in enumerate(risultati):
            print(f"Posizione {i+1}: {risultato}")

        ripeti = input("Vuoi ripetere l'operazione? (s/n): ")
        if ripeti.lower() != 's':
            break

# Avvia il programma
if __name__ == "__main__":
    main()
