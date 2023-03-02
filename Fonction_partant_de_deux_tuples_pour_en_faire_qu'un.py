

"""ici il est cherché à combiner deux tuples en un seul 
en traitant les valeurs contenues dans les tuples 
pour les ajouter à une nouvelle liste"""

def ma_fonction(*valeurs):
    liste = []
    for t in valeurs:
        liste.extend(t)
    resultat = tuple(liste)
    print("Le paramètre est un tuple valant :", resultat)

ma_fonction((1,3),(4,5))