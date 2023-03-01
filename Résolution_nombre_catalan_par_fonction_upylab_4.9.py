
""" Résolution nombre catalan par fonction

Nous vous demandons d’écrire une fonction catalan(n), 
où n est un nombre entier positif ou nul, 
qui renvoie la valeur du  n-ième nombre de Catalan.

Exemple 1
L'appel suivant de la fonction :

catalan(5)
doit retourner

42 
Exemple 2
L'appel suivant de la fonction :

catalan(0)
doit retourner

1"""

import math

def catalan(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return int((math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))))
