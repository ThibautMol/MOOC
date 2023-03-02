
"""Écrire une fonction distance_points() qui reçoit en paramètres deux tuples 
de deux composantes représentant les coordonnées de deux points et qui 
retourne la distance euclidienne séparant ces deux points.

Pour rappel, la distance euclidienne entre les points (x_1, y_1) et (x_2, y_2) se calcule grâce à la formule :

dist = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}

où, si a désigne un nombre positif, \sqrt{a} désigne la racine carrée de a et correspond à a^{\frac{1}{2}}.

Exemple 1
L’appel suivant de la fonction :

distance_points((1.0, 1.0), (2.0, 1.0))
doit retourner :

1.0
Exemple 2
L’appel suivant de la fonction :

distance_points((-1.0, 0.5), (2.0, 1.0))
doit retourner (approximativement) :

3.0413812651491097"""

import math

def distance_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist
