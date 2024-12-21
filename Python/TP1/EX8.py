# Exercice 8 : Fonctions variadiques

def somme_varargs(*args):
    return sum(args)

# Exemple d'utilisation
print(somme_varargs(1, 2, 3, 4))  # Affiche 10