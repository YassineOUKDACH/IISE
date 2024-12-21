# Exercice 4 : Dictionnaires

def compte_occurences(liste):
    return {mot: liste.count(mot) for mot in set(liste)}

# Exemple d'utilisation
print(compte_occurences(['a', 'b', 'a', 'c', 'b']))  # Affiche {'a': 2, 'b': 2, 'c': 1}