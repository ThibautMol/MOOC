"""Jeu de la roulette comme demandée par le MOOC"""

a=int(input())
b=int(input())

if a>=0 and a<=12 :
    if a==b : print(10*12)
    else : print("0")

if a==13 :
    if b%2==0 :
        print(10*2)
    else :
        print("0")

if a==14 :
    if b%2!=0 :
        print(10*2)
    else :
        print("0")

if a==15 :
    if b==1 :
        print(10*2)
    elif b==3 :
        print(10 * 2)
    elif b==5 :
        print(10 * 2)
    elif b==7 :
        print(10 * 2)
    elif b==9 :
        print(10 * 2)
    elif b==12 :
        print(10 * 2)
    else :
        print("0")

if a==16 :
    if b==2 :
        print(10*2)
    elif b==4 :
        print(10 * 2)
    elif b==6 :
        print(10 * 2)
    elif b==8 :
        print(10 * 2)
    elif b==10 :
        print(10 * 2)
    elif b==11 :
        print(10 * 2)
    else :
        print("0")