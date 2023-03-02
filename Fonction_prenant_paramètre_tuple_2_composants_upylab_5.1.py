
"""Écrire une fonction signature qui reçoit un paramètre identite . 
Ce paramètre est un couple (tuple de deux composantes) dont la première composante représente un nom et la seconde un prénom.

Cette fonction doit retourner la chaîne de caractères formée du prénom suivi du nom, séparés par une espace.

Exemple
L’appel suivant de la fonction :

signature(('de Saint-Exupéry', 'Antoine'))
doit retourner :

'Antoine de Saint-Exupéry'
"""
#version initiale : 

def signature(identite):
    return identite[1] + " " + identite[0]

def signature (identite):
    nom, prenom=identite
    return prenom + ' ' + nom

#Version plus sexy : 

from typing import Tuple

def signature(identite: Tuple[str, str]) -> str:
    nom, prenom = identite
    return prenom + " " + nom