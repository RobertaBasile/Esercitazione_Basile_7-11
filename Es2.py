class Collezione:
    def __init__(self):
        self.__elementi = []

    def aggiungi_elemento(self, elemento):
        self.__elementi.append(elemento)

    def elementi_unici(self):
        unici = []
        duplicati = set()
        for elemento in self.__elementi:
            if elemento not in duplicati:
                if self.__elementi.count(elemento) == 1:
                    unici.append(elemento)
                else:
                    duplicati.add(elemento)
        return unici

    def mostra_elementi_unici(self):
        unici = self.elementi_unici()
        print("Elementi unici nella collezione:", unici)

def main():
    collezione = Collezione()
    ripetizioni = int(input("Quanti elementi vuoi inserire? "))

    for _ in range(ripetizioni):
        elemento = input("Inserisci una parola o un numero: ")
        try:
            elemento = int(elemento)
        except ValueError:
            try:
                elemento = float(elemento)
            except ValueError:
                pass
        collezione.aggiungi_elemento(elemento)

    collezione.mostra_elementi_unici()

# Avvia il programma
if __name__ == "__main__":
    main()
