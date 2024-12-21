### 8. Classe `Vehicule` avec Méthodes Abstraites


from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass

class Voiture(Vehicule):
    def deplacer(self):
        print("La voiture roule sur la route.")

class Bicyclette(Vehicule):
    def deplacer(self):
        print("La bicyclette avance en pédalant.")

# Exemple d'utilisation
vehicules = [Voiture(), Bicyclette()]
for vehicule in vehicules:
    vehicule.deplacer()