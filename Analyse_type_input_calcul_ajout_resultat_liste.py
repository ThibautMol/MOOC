
"""Écrire une fonction my_pow qui prend comme paramètres un nombre entier m et un nombre flottant b, 
et qui renvoie une liste contenant les m premières puissances de b, 
c’est-à-dire une liste contenant les nombres allant de b^0 à b^{m - 1}.

Si le type des paramètres n’est pas celui attendu, la fonction retournera la valeur None.

Exemple 1
L’appel suivant de la fonction :

my_pow(3, 5.0)
doit retourner :

[1.0, 5.0, 25.0]
Exemple 2
L’appel suivant de la fonction :

my_pow(3.0, 5.0)
doit retourner :

None
Exemple 3
L’appel suivant de la fonction :

my_pow('a', 'b')
doit retourner :

None"""



"""V1 possédant des blocages

m=int(input())
b=float(input())
my_list=[]

def my_pow (m,b) :
    if type(m) != int or type (b) != float :
        return None
    else :
        for i in range (0,m) :
            my_list.append(b**i)
            return my_list

my_pow(m,b)
print(my_list)
"""

# V2 Fonctionnelle 

def my_pow(m, b):
    if type(m) != int or type(b) != float:
        return None
    else:
        return [b**i for i in range(m)]
