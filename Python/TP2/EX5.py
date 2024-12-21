class Animal:
    def faire_du_bruit(self):
        pass

class Chien(Animal):
    def faire_du_bruit(self):
        print("Woof!")

class Chat(Animal):
    def faire_du_bruit(self):
        print("Meow!")

# Exemple d'utilisation
chien = Chien()
chat = Chat()
chien.faire_du_bruit()
chat.faire_du_bruit()