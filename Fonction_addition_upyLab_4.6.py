"""définition d'une fonction additionnant deux chiffres mis en input 
sinon additionnant les valeurs par défaut fournies

Écrire une fonction somme(a, b) qui retourne la somme de deux valeurs entières a et b. 
Par défaut, la valeur de a est 0 et la valeur de b est 1.

Exemple 1
L’appel suivant de la fonction :

somme(24, 18)
doit retourner :

42
Exemple 2
L’appel suivant de la fonction :

somme(4)
doit retourner :

5
Exemple 3
L’appel suivant de la fonction :

somme()
doit retourner :

1"""

def somme(a=0,b=1) :
    return a+b
   

a=input()
b=input()

result=somme(int(a),int(b))
print(result)