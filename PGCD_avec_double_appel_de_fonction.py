"""PGCD avec double appel de fonction"""


def pgcd(x, y):
    """Calcule le pgcd de 2 entiers x et y positifs"""
    while (y > 0):
       x, y  =  y, x % y
    return x

print('le pgcd de 112 et de 30 vaut : ', pgcd(112, 30)) #code "appelant"
a = int(input(" a = "))
if pgcd(a, 6) == 2:
   print("le pgcd est égal à 2")
else:
   print("le pgcd est différent de 2")