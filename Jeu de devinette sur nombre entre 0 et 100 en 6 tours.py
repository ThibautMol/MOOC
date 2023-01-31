"""Jeu de devinette sur nombre entre 0 et 100 en 6 tours"""

import random
nombre_devinette=random.randint(0,100)
nombre_tour=0
while True :
    nombre_joueur=int(input())
    nombre_tour=nombre_tour+1
    if nombre_tour == 6:
        break
    elif nombre_joueur>nombre_devinette :
        print("Trop grand")
    elif nombre_joueur<nombre_devinette :
        print("Trop petit")
    elif nombre_joueur==nombre_devinette :
        break
if nombre_devinette==nombre_joueur :
    print("Gagné en",nombre_tour,"essai(s) !")
else :
    print("Perdu ! Le secret était", nombre_devinette)