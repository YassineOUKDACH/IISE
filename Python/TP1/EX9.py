# Solutions aux Exercices Combinés

# Exercice 9 : Analyser un texte

def analyse_texte(texte):
    mots = texte.split()
    return {
        "nombre_de_mots": len(mots),
        "nombre_de_caracteres": len(texte)
    }

# Exemple d'utilisation
print(analyse_texte("Bonjour tout le monde"))  # Affiche {'nombre_de_mots': 4, 'nombre_de_caracteres': 22}