"""PGCD avec fonction"""

def pgcd (x,y) :
    """Calcule le PGCD de deux entiers X et Y positifs"""
    while y > 0 :
        x, y = y, x % y
    return x


#Lecture des données

x=int(input('x ='))
y=int(input('y='))

#Calcul du PGCD
le_pgcd=pgcd(x,y)

#Affichage du résultat
print('PGCD vaut :', le_pgcd)