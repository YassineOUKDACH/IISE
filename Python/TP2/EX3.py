class CompteBancaire:
    def __init__(self, titulaire):
        self.titulaire = titulaire
        self.solde = 0

    def deposer(self, montant):
        self.solde += montant
        print(f"Dépôt de {montant} €. Nouveau solde: {self.solde} €.")

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"Retrait de {montant} €. Nouveau solde: {self.solde} €.")
        else:
            print("Fonds insuffisants.")

    def afficher_solde(self):
        print(f"Solde actuel: {self.solde} €.")

# Exemple d'utilisation
compte = CompteBancaire("Alice")
compte.deposer(100)
compte.retirer(30)
compte.afficher_solde()
