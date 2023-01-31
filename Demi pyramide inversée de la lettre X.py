"""Demi pyramide inversée de la lettre X
   l'input détermine la hauteur de la pyramide"""

n=int(input())
y=n
t=0
while True :
    print((t*" "),sep='', end='',)
    print(str(n * "X"))
    n=n-1
    y=y-1
    t=t+1
    if n==0 :
     break