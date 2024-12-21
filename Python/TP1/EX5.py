# Exercice 5 : Fonction récursive

def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

# Exemple d'utilisation
print(factorielle(5))  # Affiche 120