"""Commentaire pluviométrie
   en fonction de la pluviométrie mise en input
   un commentaire différent est généré"""

maximum=0
print("pluviométrie : ")
releve = int(input())
if releve==0:
    print("pas de pluie aujourd'hui")
elif releve>maximum:
    maximum=releve
    print("Nous avons un nouveau record")
else:
    print("pas de nouveau record")
print("Maximum retenu :",maximum)