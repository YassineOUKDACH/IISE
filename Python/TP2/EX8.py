class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []

    def ajouter_ami(self, ami):
        self.amis.append(ami)

    def afficher_amis(self):
        print(f"Ami(s) de {self.prenom} :")
        for ami in self.amis:
            print(f"- {ami.prenom} {ami.nom}")

# Exemple d'utilisation
personne1 = Personne("Dupont", "Jean", 25)
personne2 = Personne("Martin", "Sophie", 22)
personne1.ajouter_ami(personne2)
personne1.afficher_amis()