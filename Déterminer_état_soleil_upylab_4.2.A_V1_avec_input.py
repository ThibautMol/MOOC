"""Déterminer moment de la journée
    
    Programme visant à déterminer si pour une heure donnée le soleil est levé ou couché 
    afin de savoir si l'on peut voir des aurores boréales ou pas"""

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

heure_lever=input("Heure de levé de soleil :")
heure_coucher=input("Heure de coucher du soleil :")
heure_actuelle=input("Heure actuelle :")

result=soleil_leve(heure_lever, heure_coucher, heure_actuelle)
print("Possibilité de voir des aurores boréales :",result)