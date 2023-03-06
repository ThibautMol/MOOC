

"""Écrire une fonction prime_numbers qui reçoit comme paramètre un nombre entier nb et 
qui renvoie la liste des nb premiers nombres premiers.

Si le paramètre n’est pas du type attendu, ou ne correspond pas à un nombre entier positif ou nul, 
la fonction renvoie None.

Exemple 1
L’appel suivant de la fonction :

prime_numbers(4)
doit retourner :

[2, 3, 5, 7]
Exemple 2
L’appel suivant de la fonction :

prime_numbers(-2)
doit retourner :

None"""



def prime_numbers(nb):
    """Returns a list of nb prime numbers"""
    if not isinstance(nb, int) or nb < 0: #isinstance prend deux éléments : une variable et un type et vérifie si les deux correspondent.
        return None #ce if permet de vérifier à la fois qu'il s'agit bien d'un int mais également qu'il est supérieur à 0
    primes = []
    i = 2 #initialisation de i à 2 car c'est le plus petit nombre pair
    while len(primes) < nb:
        is_prime = True #initialisation de la variable is_prime en true
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False #vérification si le nombre est bien premier
                break
        if is_prime: #si is_prime reste true, alors on ajoute le chiffre à la liste primes.
            primes.append(i)
        i += 1
    return primes
