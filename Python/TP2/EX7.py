class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        for livre in self.livres:
            print(f"{livre.titre} par {livre.auteur} ({livre.annee_publication})")

# Exemple d'utilisation
bibliotheque = Bibliotheque()
livre1 = Livre("1984", "George Orwell", 1949)
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.afficher_livres()
