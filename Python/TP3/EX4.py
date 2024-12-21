from abc import ABC, abstractmethod
import math

class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    def appliquer_remise(self, remise):
        if self.__prix > 100:
            self.__prix -= self.__prix * (remise / 100)

    def get_prix(self):
        return self.__prix

# Exemple d'utilisation
produit = Produit("Laptop", 1200)
produit.appliquer_remise(10)
print(f"Prix après remise: {produit.get_prix()} €")