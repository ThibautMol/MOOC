
"""Joao vient d’arriver dans notre pays depuis le Portugal. 
Il a encore du mal avec la langue française. 
Malgré ses efforts considérables, il fait une faute d’orthographe quasi à chaque mot. 
Son souci est qu’il n’arrive pas toujours à écrire un mot correctement sans se tromper à une lettre près. 
Ainsi pour écrire « bonjour », il peut écrire « binjour ». 
Pour remédier à ce problème, Joao utilise un correcteur orthographique. 
Malheureusement, Joao a un examen aujourd’hui et il a oublié son petit correcteur.

Afin de l’aider, nous vous demandons d’écrire une fonction correcteur(mot, liste_mots)
 où mot est le mot que Joao écrit et liste_mots est une liste qui contient 
 les mots (ayant la bonne orthographe) que Joao est susceptible d’utiliser.

Cette fonction doit retourner le mot dont l’orthographe a été corrigée.

Exemple 1
L’appel suivant de la fonction :

correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"])
doit retourner :

"bonjour"
Exemple 2
L’appel suivant de la fonction :

correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"])
doit retourner :

"chat""""

def distance_mots(mot_1, mot_2):
    distance = 0
    for i in range(len(mot_1)):
        if mot_1[i] != mot_2[i]:
            distance += 1
    return distance


def correcteur(mot, liste_mots):
    """Corrige un mot avec une distance d'édition d'une lettre."""
    for mot_ref in liste_mots:
        if len(mot_ref) == len(mot) and distance_mots(mot, mot_ref) == 1:
            return mot_ref
    return mot
