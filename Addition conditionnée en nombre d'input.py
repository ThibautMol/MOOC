"""Addition de valeurs en input
   Le premier nombre entré détermine le nombre d'input à calculer
   Si le première nombre entré est -1, il faudra mettre F en input pour stopper la demande d'input
   Le total est print une fois le nombre de valeurs entrées"""

nombre_entrees=int(input())
total=0
if nombre_entrees !=-1 :
    for i in range(nombre_entrees) :
        total=int(input())+total #version alternative total+=int(input())
else :
    while nombre_entrees == -1 :
        y=input()
        if y=="F" :
            break
        total = int(y) + total


print(int(total))