
"""Écrire une fonction my_insert qui reçoit comme premier paramètre une liste d’entiers relatifs 
triée par ordre croissant et comme deuxième paramètre un entier relatif n, 
et qui renvoie une liste correspondant à la liste reçue, mais dans laquelle le nombre n a été inséré à la bonne place.

La liste donnée en paramètre ne doit pas être modifiée par votre fonction.

Vous pouvez supposer que le premier paramètre sera bien une liste triée d’entiers, 
mais si le deuxième paramètre n’est pas du bon type, la fonction retourne None.

L’exercice est le même que le précédent, mais ici, si les paramètres ont le type attendu, 
la fonction modifie la liste en place et ne retourne rien. 
Si les paramètres ne sont pas valides, une erreur se produit à l’exécution.

Exemple 1
L’exécution du code suivant :

l = [1, 3, 5]
my_insert(l, 4)
print(l)
doit afficher :

[1, 3, 4, 5]
Exemple 2
L’exécution du code suivant :

l = [1, 3, 5]
my_insert(l, 'a')
print(l)
doit provoquer une exception Python, par exemple :

AssertionError"""

def my_insert(lst, n):
    # Vérifier que le premier paramètre est bien une liste d'entiers triée
    assert isinstance(lst, list) and all(isinstance(x, int) for x in lst) and lst == sorted(lst), "Le premier paramètre doit être une liste d'entiers triée"

    # Vérifier que le deuxième paramètre est bien un entier
    assert isinstance(n, int), "Le deuxième paramètre doit être un entier"

    # Insérer l'entier n à la bonne place dans la liste lst
    for i in range(len(lst)):
        if lst[i] >= n:
            lst.insert(i, n)
            return
    lst.append(n)
