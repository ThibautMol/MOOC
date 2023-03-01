
"""Écrire un programme qui réalise 5 manches du jeu Pierre-feuille-ciseaux entre l’ordinateur et le joueur. 

Chaque manche va consister en :

la génération (pseudo) aléatoire d’un nombre entre 0 et 2 compris, à l’aide de la fonction randint du module random, 
qui va représenter le coup de l’ordinateur (0 valant Pierre, 1, Feuille et 2, Ciseaux) ;

la lecture en entrée (input) d’une valeur entière entre 0 et 2 compris qui représente le coup du joueur ;

l’affichage du résultat sous une des formes :

coup_o bat coup_j : points

coup_o est battu par coup_j : points

coup_o annule coup_j : points

où

coup_o et coup_j sont respectivement le coup de l’ordinateur et du joueur : 
"Pierre" s’il a joué 0, "Feuille" s’il a joué 1 et "Ciseaux" s’il a joué 2.

points donne le résultat des manches jusqu’à présent sachant que le compteur points part de zéro, 
et est incrémenté de un chaque fois que le joueur gagne une manche, 
et décrémenté de un chaque fois que l’ordinateur gagne une manche (les match nuls ne modifiant pas le compteur points).

À la fin des cinq manches, votre programme affichera : 
Perdu, Nul ou Gagné suivant que le compteur est négatif, nul ou strictement positif."""


import random

PIERRE = 0
FEUILLE = 1
CISEAUX = 2

# Fonction qui renvoie le résultat de la manche et met à jour le compteur de points

def jouer_manche(coup_joueur, coup_ordi, points):

    if coup_joueur == coup_ordi:
        print(noms_coups[coup_joueur], "annule", noms_coups[coup_ordi], ":", points)

    elif (coup_joueur == PIERRE and coup_ordi == CISEAUX) or \
        (coup_joueur == FEUILLE and coup_ordi == PIERRE) or \
        (coup_joueur == CISEAUX and coup_ordi == FEUILLE):
        points += 1
        print(noms_coups[coup_ordi], "est battu par", noms_coups[coup_joueur], ":", points)

    else:
        points -= 1
        print(noms_coups[coup_ordi], "bat", noms_coups[coup_joueur], ":", points)

    return points

# Initialisation des noms des coups
noms_coups = ["Pierre", "Feuille", "Ciseaux"]

# Initialisation du compteur de points
points = 0

# Réalisation des 5 manches
for i in range(5):
    coup_ordi = random.randint(0, 2)
    coup_joueur = int(input())
    points = jouer_manche(coup_joueur, coup_ordi, points)

# Affichage du résultat final
if points > 0:
    print("Gagné")
elif points == 0:
    print("Nul")
else:
    print("Perdu")
