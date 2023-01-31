"""Faire un cube avec la lettre x
   L'input détermine la hauteur et largeur du cube"""

n=int(input())
y=n
while True :
    print(n*"X")
    y=y-1
    z=y-1
    if z==-1 :
        break