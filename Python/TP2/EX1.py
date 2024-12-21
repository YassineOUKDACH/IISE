class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age

    def aboyer(self):
        print("Woof!")

# Exemple d'utilisation
mon_chien = Chien("Rex", "Berger Allemand", 5)
mon_chien.aboyer()
