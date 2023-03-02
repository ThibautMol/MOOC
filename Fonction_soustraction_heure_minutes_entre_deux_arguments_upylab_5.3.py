
"""Écrire une fonction duree qui reçoit deux paramètres debut et fin. 
Ces derniers sont des couples (tuples de deux composantes) 
dont la première composante représente une heure et la seconde les minutes.

Cette fonction doit calculer la durée qui s’est écoulée entre ces deux instants. 
Le résultat sera donné sous la forme d’un tuple (heure, minutes).

Exemple 1
L’appel suivant de la fonction :

duree ((14, 39), (18, 45))
doit retourner :

(4, 6)
Exemple 2
L’appel suivant de la fonction :

duree ((6, 0), (5, 15))
doit retourner :

(23, 15)"""

def duree(debut,fin) :
    heures=(debut[0]-fin[0])
    minutes=(debut[1]-fin[1])

    if minutes < 0 :
        heures-=1
        minutes +=60

    if heures < 0 :
        heures +=24
    
    return (heures, minutes)


