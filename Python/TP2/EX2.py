class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(f"{self.marque} {self.modele}, {self.annee}")

# Exemple d'utilisation
voiture1 = Voiture("Toyota", "Corolla", 2020)
voiture2 = Voiture("Ford", "Mustang", 2021)
voiture1.afficher_info()
voiture2.afficher_info()