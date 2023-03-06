

""""Écrire une fonction anagrammes(v, w) qui renvoie la valeur booléenne True 
si les mots v et w sont des anagrammes.

La fonction retourne la valeur booléenne False dans le cas contraire.

Exemple 1
L’appel suivant de la fonction :

anagrammes('marion', 'romina')
doit retourner :

True
Exemple 2
L’appel suivant de la fonction :

anagrammes('bonjour', 'jour')
doit retourner :

False
Exemple 3
L’appel suivant de la fonction :

anagrammes('pate', 'patte')
doit retourner :

False"""

#fonction V2 fonctionnelle

def anagrammes(v, w):
    if len(v) != len(w):  # Vérifie que les deux chaînes ont la même longueur
        return False
    
    for c in v:
        if v.count(c) != w.count(c):  # Compare la quantité de chaque lettre dans les deux chaînes
            return False
    
    return True




#fonction V1 non-aboutie

def anagrammes(v,w) :
    value_anagramme = True
    for i in range(len(v)) :
        if  v[i] in w :
            value_anagramme = True
            i+=1
        else :
            value_anagramme = False
    return value_anagramme

anagrammes(input(),input())
