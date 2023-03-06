
"""Écrire une fonction distance_mots(mot_1, mot_2) 
qui retourne la distance entre deux mots.

Vous pouvez supposer que les deux mots sont de même longueur, 
et sont écrits sans accents.

Exemple 1
L’appel suivant de la fonction :

distance_mots("lire", "bise")
doit retourner :

2
Exemple 2
L’appel suivant de la fonction :

distance_mots("Python", "Python")
doit retourner :

0
Exemple 3
L’appel suivant de la fonction :

distance_mots("merci", "adieu")
doit retourner :

5
Exemple 4
L’appel suivant de la fonction :

distance_mots("chien", "niche")
doit retourner :

5"""

def distance_mots(mot_1, mot_2) :
    
    distance=0
    
    if len(mot_1)==len(mot_2) :
     
        for i in range (len(mot_1)) :
            if mot_1[i]==mot_2[i] :
                distance+=0
            else :
                distance+=1

    return distance