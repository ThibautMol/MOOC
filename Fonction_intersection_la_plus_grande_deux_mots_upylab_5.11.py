
"""Écrire une fonction intersection(v, w) qui calcule l’intersection 
entre deux chaînes de caractères v et w.

On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots. 
Par exemple, l’intersection de « programme » et « grammaire » est « gramm ».

Si les deux chaînes n’ont aucun caractère en commun, la fonction retourne la chaîne vide, ''.

Si plusieurs solutions sont possibles, la fonction retournera la sous-chaîne d’indice minimal dans v. 
Par exemple, intersection('bbaacc', 'aabb') renvoie 'bb'.

Exemple 1
L’appel suivant de la fonction :

intersection('programme', 'grammaire')
doit retourner :

'gramm'
Exemple 2
L’appel suivant de la fonction :

intersection('salut', 'merci')
doit retourner :

''
Exemple 3
L’appel suivant de la fonction :

intersection('merci', 'adieu')
doit retourner :

'e'"""

def intersection(v, w):
    # Initialise la chaîne d'intersection avec une chaîne vide
    intersection = ''
    
    # Parcours tous les sous-mots possibles de v et w
    for i in range(len(v)):
        for j in range(len(w)):
            k = 0
            # Compare les caractères correspondants de v et w pour trouver l'intersection
            while i+k < len(v) and j+k < len(w) and v[i+k] == w[j+k]:
                k += 1 #on va incrémenter k tant qu'on obtient une égalité entre les caractères. Si non k n'est pas incrémenté
            # Met à jour la chaîne d'intersection si la longueur de l'intersection est plus grande
            if k > len(intersection):
                intersection = v[i:i+k] #boucle if dans la while afin de rentrer la valeur d'égalité trouvée dans le while. 
    
    # Retourne la plus grande intersection trouvée
    return intersection
