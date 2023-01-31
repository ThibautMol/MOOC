"""jeu de la roulette conditionnée par la formation MOOC
   le numéro choisi en input détermine le jeu auquel la personne souhaite jouer
   il peut parier sur le chiffre, la couleur, pair ou impair"""
import random
tirage_nbr=random.randint(0,12)
nbr_joueur=int(input("Choisissez votre numéro"))
print("numéro tirage",tirage_nbr)

if nbr_joueur>=0 and nbr_joueur<=12 :
    if tirage_nbr==nbr_joueur :
        print("gains :",10*12)
    else :
        print("perdu mauvais numéro")
elif nbr_joueur==13 :
    if tirage_nbr%2==0 :
        print("gagné c'est pair")
        print("gains :", 10*2)
    else :
        print("perdu c'est impair")
elif nbr_joueur==14 :
    if tirage_nbr%2!=0 :
        print("gagné c'est impair")
        print("gains :", 10 * 2)
    else :
        print("perdu c'est pair")
elif nbr_joueur==15 :
    if tirage_nbr== 1 or tirage_nbr==3 or tirage_nbr==5 or tirage_nbr==7 or tirage_nbr==9 or tirage_nbr==12 :
        print("gagné c'est rouge")
        print("gains :", 10 * 2)
    else :
        print("perdu c'est noir")
elif nbr_joueur==16 :
    if tirage_nbr==2 or tirage_nbr==4 or tirage_nbr==6 or tirage_nbr==8 or tirage_nbr==10 or tirage_nbr==11 :
        print("gagné c'est noir")
        print("gains :", 10 * 2)
    else :
        print("perdu c'est rouge")