"""Lecture nombre premier + print liste nombres premiers inférieurs

Écrire une fonction booléenne premier(n) qui reçoit un nombre entier positif n et qui renvoie True si n est un nombre premier, et False sinon.

Ensuite, écrire un programme qui lit une valeur entière x et affiche, 
grâce à des appels à la fonction premier, 
tous les nombres premiers strictement inférieurs à x, chacun sur sa propre ligne."""

def premier(n):
    """
    Vérifie si n est un nombre premier.

    Args:
        n (int): un entier positif

    Returns:
        bool: True si n est un nombre premier, False sinon
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

x = int(input())
for i in range(2, x):
    if premier(i):
        print(i)
