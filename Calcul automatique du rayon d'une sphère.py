"""Calcul automatique du rayon d'une sphère
    Utilisation du module pi de Python
    Variable r correspond au rayon donné en input
    Impression du résultat en fin de calcul"""

from math import pi
r=float(input())
print(4/3*(pi)*r**3)