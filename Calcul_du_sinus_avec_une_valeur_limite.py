"""Calcul du sinus avec une valeur limite""""

x=float(input())
valeur_limite=10**-6
fact = 1
n=1
sin_x=0
for i in range (0, n+1) :
    n=n+1
    for j in range(2, n + 1):
        fact = fact * j
        sin_x=x**fact/fact
        if sin_x<valeur_limite :
            break
    if sin_x < valeur_limite:
        break
print(sin_x)