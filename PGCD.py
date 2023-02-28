"""PGCD"""

#Lecture des données

x=int(input('x ='))
y=int(input('y='))

#Calcul effectif PGCD
while y > 0 :
    x, y = y, x % y

#Affichage du résultat
print('PGCD vaut :', x)