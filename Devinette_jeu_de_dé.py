"""Devinette jeu de dé"""

import random
secret=random.randint(0,5)
print("Quelle est votre nombre entre 0 et 5?")
x=int(input())
if x==secret :
    print("Vous avez gagné")
else :
    print("vous avez perdu")
    print("Le bon numéro était", secret)