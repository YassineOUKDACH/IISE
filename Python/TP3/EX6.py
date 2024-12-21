### 7. Système de Gestion de Commandes


class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total(self):
        total = sum(commande.produit.prix * commande.quantite for commande in self.commandes)
        return total


# Exemple d'utilisation
produit1 = Produit("Laptop", 1200)
produit2 = Produit("Smartphone", 800)
commande1 = Commande(produit1, 1)
commande2 = Commande(produit2, 2)

panier = Panier()
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)
print(f"Total du panier: {panier.calculer_total()} €")
