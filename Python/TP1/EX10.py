# Exercice 10 : Fusionner des dictionnaires

def fusionner_dicts(dict1, dict2):
    fusion = dict1.copy()  # Copie le premier dictionnaire
    for key, value in dict2.items():
        if key in fusion:
            fusion[key] += value
        else:
            fusion[key] = value
    return fusion

# Exemple d'utilisation
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(fusionner_dicts(dict1, dict2))  # Affiche {'a': 1, 'b': 5, 'c': 4}