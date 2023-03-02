
"""Écrire une fonction longueur(*points) 
qui reçoit en paramètres un nombre arbitraire de points (tuples de deux composantes), 
et retourne la longueur de la ligne brisée correspondante.

Cette longueur se calcule en additionnant les longueurs des segments 
formés par deux points consécutifs.

Exemple 1
L’appel suivant de la fonction :

longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0))
doit retourner :

2.0
Exemple 2
L’appel suivant de la fonction :

longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0))
doit retourner (approximativement) :

7.1122677042334645"""


import math

def longueur(*points):
    longueur_totale = 0.0
    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        segment_length = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        longueur_totale += segment_length
    return longueur_totale
