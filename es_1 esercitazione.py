class GestoreDati:
    def __init__(self):
        self.numeri = []
        self.stringhe = []
        self.booleani = []

    def aggiungi_dato(self, dato):
        if isinstance(dato, (int, float)):
            self.numeri.append(dato)
        elif isinstance(dato, str):
            self.stringhe.append(dato)
        elif isinstance(dato, bool):
            self.booleani.append(dato)
        else:
            print("Tipo di dato non supportato.")

    def stampa_lista(self, tipo):
        if tipo == "numeri":
            print("Lista dei numeri:", self.numeri)
        elif tipo == "stringhe":
            print("Lista delle stringhe:", self.stringhe)
        elif tipo == "booleani":
            print("Lista dei booleani:", self.booleani)
        else:
            print("Tipo di lista non valido.")

    def stampa_tutte_liste(self):
        print("Lista dei numeri:", self.numeri)
        print("Lista delle stringhe:", self.stringhe)
        print("Lista dei booleani:", self.booleani)

# Esempio
gestore = GestoreDati()
gestore.aggiungi_dato(42)
gestore.aggiungi_dato("ciao")
gestore.aggiungi_dato(True)
gestore.aggiungi_dato(3.14)
gestore.aggiungi_dato("mondo")
gestore.aggiungi_dato(False)

gestore.stampa_lista("numeri")
gestore.stampa_lista("stringhe")
gestore.stampa_lista("booleani")
gestore.stampa_tutte_liste()