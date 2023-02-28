""""Programme visant à calculer si les deux soleils sont levés ou couchés en même temps. """

def soleil_leve(heure_lever, heure_coucher, heure_actuelle):
    if heure_lever == heure_coucher:
        if heure_lever == 12:
            return False
        elif heure_lever == 0:
            return True
    elif heure_lever < heure_coucher:
        return heure_actuelle >= heure_lever and heure_actuelle < heure_coucher
    else:
        return heure_actuelle >= heure_lever or heure_actuelle < heure_coucher

# Lecture des heures de lever et coucher pour chaque soleil
heure_lever_1515 = int(input())
heure_coucher_1515 = int(input())
heure_lever_666 = int(input())
heure_coucher_666 = int(input())

# Boucle pour afficher chaque heure de la journée
for heure in range(24):
    if soleil_leve(heure_lever_1515, heure_coucher_1515, heure) or soleil_leve(heure_lever_666, heure_coucher_666, heure):
        # Si l'un ou l'autre des soleils est levé, on affiche simplement l'heure
        print(heure)
    else:
        # Si les deux soleils sont couchés, on affiche l'heure suivie d'une astérisque
        print(str(heure) + " *")
