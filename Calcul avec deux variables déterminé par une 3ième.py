"""Calcul avec deux variables déterminé par une 3ième
    c détermine le calcul opéré en fonction de 4 solutions"""


a=int(input())
b=int(input())
c=int(input())
if c==1 :
    print(a+b)
elif c==2 :
    print(a-b)
elif c==3 :
    print(a*b)
elif c==4 :
    print(a**2+a*b)
else :
    print("Erreur")