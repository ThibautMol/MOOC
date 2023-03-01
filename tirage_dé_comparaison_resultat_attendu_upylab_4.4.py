
"""Écrire une fonction alea_dice(s) qui génère trois nombres (pseudo) aléatoires à l’aide de la fonction randint du module random, 
représentant trois dés (à six faces avec les valeurs de 1 à 6), 
et qui renvoie la valeur booléenne True si les dés forment un 421, 
et la valeur booléenne False sinon.

Le paramètre s de la fonction est un nombre entier, 
qui sera passé en argument à la fonction random.seed au début du code de la fonction. 
Cela permettra de générer la même suite de nombres aléatoires à chaque appel de la fonction, 
et ainsi de pouvoir tester son fonctionnement."""


def alea_dice(s):
    random.seed(s)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    return sorted([dice1, dice2, dice3]) == [1, 2, 4] 
    """utilisation de la fonction sorted permet de ranger la valeur des tirages par ordre croissant 
    afin de les comparé à celles définies car les chiffres peuvent être générés dans n'importe quel ordre par le tirage"""