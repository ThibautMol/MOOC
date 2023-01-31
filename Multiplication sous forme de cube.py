"""Table de multiplication sous forme de cube"""

n=int(input())
for i in range(1,n+1) : #défini la première colonne verticale
    for j in range(1,n+1) : #cette fonction va définir ce qui est inscrit sur chaque ligne horizontale du i
        print(j*i, end=' ')
    print() #ce print dans le for i in range va permettre de faire une mise à la ligne des données du j