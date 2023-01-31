"""Calcul du volume d'un polyèdre
   en fonction de l'initiale du polyèdre
   le calcul adapté s'appliquera"""

from math import sqrt
nom_Polyedre=input()
a=float(input())
if nom_Polyedre=="T" :
    v=(sqrt(2)/12)*a**3
    print(v)
elif nom_Polyedre=="C" :
    v=a**3
    print(v)
elif nom_Polyedre=="O" :
    v=(sqrt(2)/3)*a**3
    print(v)
elif nom_Polyedre=="D" :
    v=(15+7*(sqrt(5)))/4*a**3
    print(v)
elif nom_Polyedre=="I" :
    v=5*(3+(sqrt(5)))/12*a**3
    print(v)
else :
    print("Polyèdre non connu")
