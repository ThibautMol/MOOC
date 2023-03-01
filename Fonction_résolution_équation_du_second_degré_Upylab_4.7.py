""" résolution équation du second degré

Écrire une fonction rac_eq_2nd_deg(a, b, c) qui reçoit trois paramètres de type float correspondant aux trois coefficients de l’équation 
du second degré ax^2 + bx + c = 0, avec a différent de 0, 
et qui renvoie la ou les solutions s’il y en a, sous forme d’un tuple.

Exemple 1
L’appel suivant de la fonction :

rac_eq_2nd_deg(1.0,-4.0,4.0)
doit retourner :

(2.0,)
Exemple 2
L’appel suivant de la fonction :

rac_eq_2nd_deg(1.0,1.0,-2.0)
doit retourner :

(-2.0, 1.0)
Exemple 3
L’appel suivant de la fonction :

rac_eq_2nd_deg(1.0,1.0,1.0)
doit retourner :

()
"""

from math import sqrt

def rac_eq_2nd_deg(a, b, c):
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return ()
    elif discriminant == 0:
        return (-b / (2 * a),)
    else:
        racine1 = (2 * c) / (-b - sqrt(discriminant))
        racine2 = (2 * c) / (-b + sqrt(discriminant))
        return (racine1, racine2) if racine1 < racine2 else (racine2, racine1)
