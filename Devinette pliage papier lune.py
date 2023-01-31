"""Devinette combien de pliages d'une feuille pour aller sur la lune"""

nbr_pliage=42
nbr_dmd=int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
while nbr_dmd!=nbr_pliage :
        print("Mauvaise réponse.")
        nbr_dmd = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
print("Bravo !")