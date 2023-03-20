
"""On considère une liste qui décrit une séquence t. 
Chaque élément de cette liste est un tuple de deux composantes : 
le nombre de répétitions successives de l’élément x dans la séquence t, et l’élément x lui-même.

Par exemple, la liste [(1, 'He'), (2, 'l'), (1,'o')] décrit la séquence "Hello".

Écrire une fonction decompresse qui reçoit une telle liste en paramètre et renvoie la séquence t sous forme d’une nouvelle liste.

Exemple
L’appel suivant de la fonction :

decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')])
doit retourner :

[1, 1, 1, 1, 'test', 'test', 3, 3, 3, 'bonjour']

Il s'agit ici de multiplié de répéter le second argument autant de fois que spécifié dans le premier argument"""

def decompresse(sequence):
    resultat = []
    for nombre, element in sequence:
        resultat.extend([element] * nombre)
    return resultat
