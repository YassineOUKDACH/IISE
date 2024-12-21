from abc import ABC, abstractmethod

class Personne(ABC):
	def __init__(self, nom, prenom, age):
		self.__nom = nom
		self.__prenom = prenom
		self.__age = age


	def getName(self):
		return self.__nom

	def getPrenom(self):
		return self.__prenom

	def getAge(self):
		return self.__age


	def setAge(slef, age):
		if age > 0:
			self.__age = age
		else:
			print("L'age doit etre possitive")

P1 = Personne("Yassine", "Oukdach", 26)
nom = P1.getName()
prenom = P1.getPrenom()
age = P1.getAge()
print(nom, " ", prenom, " ", age)

print("------------------------------Method2------------------------------")
class Personne(ABC):
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    # Getter pour `nom`
    @property
    def nom(self):
        return self.__nom

    # Getter pour `prenom`
    @property
    def prenom(self):
        return self.__prenom

    # Getter pour `age`
    @property
    def age(self):
        return self.__age

        
    @age.setter
    def age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("L'âge doit être un nombre positif.")

P1 = Personne("Yassine", "Oukdach", 26)
print(P1.nom, P1.prenom, P1.age)  # Appelle les getters

P1.age = 30  # Appelle le setter
print(P1.age)
print("----------------------------Accès à l'attribut _protected---------------------------")
class Personne:
    def __init__(self, nom):
        self._nom = nom  
p = Personne("Amine")
print(p._nom)  # Possible, mais pas recommandé

print("----------------------------Accès à l'attribut _pivate (Name mangling)---------------------------")
class Personne:
    def __init__(self, nom):
        self.__nom = nom

p = Personne("Mounir")
# print(p.__nom)  
print(p._Personne__nom)

class Personne:
    def __init__(self, nom):
        self.__nom = nom

class Etudiant(Personne):
    def __init__(self, nom, note):
        super().__init__(nom)
        self.__nom = "Yassine"  # Attribut différent grâce au name mangling

e = Etudiant("Imade", 18)
print(e._Personne__nom)  # Yassine (attribut de la classe Personne)
print(e._Etudiant__nom)  # IMADE (attribut de la classe Etudiant)
