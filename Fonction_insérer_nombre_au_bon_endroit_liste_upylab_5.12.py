
"""Écrire une fonction my_insert qui reçoit comme premier paramètre une liste d’entiers relatifs 
triée par ordre croissant et comme deuxième paramètre un entier relatif n, 
et qui renvoie une liste correspondant à la liste reçue, mais dans laquelle le nombre n a été inséré à la bonne place.

La liste donnée en paramètre ne doit pas être modifiée par votre fonction.

Vous pouvez supposer que le premier paramètre sera bien une liste triée d’entiers, 
mais si le deuxième paramètre n’est pas du bon type, la fonction retourne None.

Exemple 1
L’appel suivant de la fonction :

my_insert([1, 3, 5], 4)
doit retourner :

[1, 3, 4, 5]
Exemple 2
L’appel suivant de la fonction :

my_insert([2, 3, 5], 1)
doit retourner :

[1, 2, 3, 5]
Exemple 3
L’appel suivant de la fonction :

my_insert([2, 3, 5], 0.5)
doit retourner :

None"""

def my_insert(lst, n):
    if not isinstance(n, int):
        return None #vérification des données insérées et de leur type
    
    res = lst[:] #création d'une copie de la liste donnée en arguments
    for i in range(len(lst)):
        if n <= lst[i]:
            res.insert(i, n) #permet d'insérer n à la bonne position en parcourant la liste jusqu'à ce qu'il soit au bon endroit,
                             #ici la valeur de i+1 sera remplacée par n uniquement dans la liste res. Ce qui permet de continuer a lire la liste initiale et de l'incrémentée
            break
    else:
        res.append(n) #cette ligne permet d'insérer n à la fin de la liste si aucun chiffre n'est plus grand que lui
    return res