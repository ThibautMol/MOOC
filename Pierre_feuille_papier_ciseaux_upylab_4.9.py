
""" Écrire une fonction bat(joueur_1, joueur_2) où joueur_1 et joueur_2 ont chacun une valeur entière 0, 1 ou 2, 
qui encode ce que le joueur a fait comme coup (0 : PIERRE, 1 : FEUILLE, 2 : CISEAUX) qui renvoie un résultat booléen :

vrai si joueur_1 bat le joueur_2 :

faux si joueur_2 bat joueur_1 ou fait match nul contre lui.

Exemple 1
L’appel suivant de la fonction :

bat(0, 0)
doit retourner :

False
Exemple 2
L’appel suivant de la fonction :

bat(0, 1)
doit retourner :

False
Exemple 3
L’appel suivant de la fonction :

bat(2, 1)
doit retourner :

True"""

def bat(joueur_1, joueur_2) :
    #pierre=0, feuille=1, ciseaux=2
    if joueur_1==0 and joueur_2==1 :
        return False
    elif joueur_1==0 and joueur_2==2 :
        return True
    elif joueur_1==joueur_2 :
        return False
    
    elif joueur_1==1 and joueur_2==0 :
        return True
    elif joueur_1==1 and joueur_2==2 :
        return False
    
    elif joueur_1==2 and joueur_2==0 :
        return False
    elif joueur_1==2 and joueur_2==1 :
        return True
   