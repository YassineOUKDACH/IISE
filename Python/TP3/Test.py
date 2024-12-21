class Exemple:
    def __init__(self):
        self.__attribut_prive = "Privé"

    # Getter
    @property
    def attribut_prive(self):
        return self.__attribut_prive

    # Setter
    @attribut_prive.setter
    def attribut_prive(self, valeur):
        self.__attribut_prive = valeur

# Exemple d'utilisation
objet = Exemple()
print(objet.attribut_prive)  # Appelle le getter, affiche : Privé

objet.attribut_prive = "Nouveau"  # Appelle le setter
print(objet.attribut_prive)  # Appelle le getter, affiche : Nouveau








