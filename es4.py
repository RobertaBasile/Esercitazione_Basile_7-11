# Classe base per le autofficine
class Autofficina:
    def ripara(self, veicolo):
        pass

# Classe figlia per autofficina specializzata in auto
class AutofficinaAuto(Autofficina):
    def ripara(self, veicolo):
        if isinstance(veicolo, Auto):
            print(f"Riparazione dell'auto {veicolo.modello} completata.")
        else:
            print("Questa autofficina ripara solo auto.")

# Classe figlia per autofficina specializzata in moto
class AutofficinaMoto(Autofficina):
    def ripara(self, veicolo):
        if isinstance(veicolo, Moto):
            print(f"Riparazione della moto {veicolo.modello} completata.")
        else:
            print("Questa autofficina ripara solo moto.")

# Classe base per i veicoli
class Veicolo:
    def __init__(self, modello):
        self.modello = modello

# Classe figlia per auto
class Auto(Veicolo):
    pass

# Classe figlia per moto
class Moto(Veicolo):
    pass

# Classe gestore delle riparazioni
class App_Riparazioni:
    def __init__(self):
        self.autofficine = []

    def aggiungi_autofficina(self, autofficina):
        self.autofficine.append(autofficina)

    def ripara_veicolo(self, veicolo):
        for autofficina in self.autofficine:
            autofficina.ripara(veicolo)

def main():
    # Creazione delle autofficine