

"""Écrire une fonction dupliques qui reçoit une séquence en paramètre.

La fonction doit renvoyer la valeur booléenne True 
si la séquence passée en paramètre contient des éléments dupliqués, 
et la valeur booléenne False sinon.

Exemple 1
L’appel suivant de la fonction :

dupliques([1, 2, 3, 4])
doit retourner :

False
Exemple 2
L’appel suivant de la fonction :

dupliques(['a', 'b', 'c', 'a'])
doit retourner :

True
Exemple 3
L’appel suivant de la fonction :

dupliques('abcda')
doit retourner :

True"""

#Fonction V2 fonctionnelle : 

def dupliques(x):
    occurrences = {}
    for elt in x: #elt est une variable temporaire permettant de stocker la valeur de x à chaque itérations
        if elt in occurrences: #s'il y a une ou des occurences on va incrémenté la valeur de elt de +1
            occurrences[elt] += 1 
        else:
            occurrences[elt] = 1 #s'il n'y a pas d'occurence on va laisser cette valeur à 1
    for count in occurrences.values(): #si la valeur contenue dans occurences est supérieure à 1 alors on renvoie true, sinon false. 
        if count > 1:
            return True
    return False


#fonction V1 quasi fonctionnelle

def dupliques(x) :
    
    for i in range(len(x)) :
        if  x[i] in x[i+1:] :
            return True
        return False

dupliques([1,5,3,4,7])
