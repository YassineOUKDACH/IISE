# Exercice 7 : Fonctions avec des arguments par défaut

def salutation(nom, message="Bonjour"):
    print(f"{message}, {nom}!")

# Exemple d'utilisation
salutation("Ali")  # Affiche "Bonjour, Alice!"
salutation("Ahmad", "Salut")  # Affiche "Salut, Bob!"