
"""Écrire une fonction est_adn qui reçoit une chaîne de caractères en paramètre et 
qui retourne True si cette chaîne de caractères n'est pas vide et peut représenter un brin d’ADN, 
False sinon.

Exemple 1
L’appel suivant de la fonction :

est_adn("ATGGT")
doit retourner :

True
Exemple 2
L’appel suivant de la fonction :

est_adn("ISA")
doit retourner :

False
Exemple 3
L’appel suivant de la fonction :

est_adn("CTaG")
doit retourner :

False"""

def est_adn(adn):
    
    if len(adn)==0
        return False

    for letter in adn :
        if letter not in ["A","C","G","T"] :
            return False
    return True