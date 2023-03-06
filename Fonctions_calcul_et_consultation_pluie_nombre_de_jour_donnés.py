""" programme qui enregistre les valeurs quotidiennes
  des pluies pour septembre, entrées (input)
  et donne ensuite les valeurs à la demande
  et le cumul du mois si on entre 0 comme jour """
# réserve la composante 0 pour enregistrer les pluies cumulées du mois


def collecte_donnees(nb_jours):
  """construit et renvoie une liste avec dans la composante i,
     les valeurs entières lues de pluie cumulée du jour i
     et en composante 0, la somme des pluies pour le mois entier
  """
  # réserve la composante 0 pour enregistrer les pluies cumulées du mois
  pluie = [0]
  # reçoit les valeurs
  for i in range(1, nb_jours + 1):  # jours 1 à nb_jours inclu
      pluie.append(int(input("pluie cumulée le " + str(i) + " du mois :")))
  # calcul la somme dans la composante 0
  pluie[0] = sum(pluie)
  return pluie  # renvoie la liste construite


def affiche_valeur(pluie, requete):
  if requete>nb_jours :
      print("Le numéro saisi n'est pas dans liste de jours") #évite les erreurs out of range

  elif type(requete) == int:  # suppose que requête est entre 0 et 31
      # et que pluie[requete] existe
      if requete == 0:  # demande pluie cumulée
          print("Pluie cumulée du mois :", pluie[requete])
      else:
          print("Pluie le", requete, ":", pluie[requete])
  
  else:  # requete est un couple de valeurs
      print("Pluie cumulée entre le", requete[0], "et le",
            requete[1], ":", sum(pluie[requete[0]: requete[1] + 1]))


# main - code principal
print("nombre de jour du mois: ")
nb_jours=int(input()) #permet de définir le nombre de jour du mois
pluies_septembre = collecte_donnees(nb_jours)  # lecture données
# délivre les informations désirées
print("Donnez le jour 'j' ou la période 'i, j'",
    "dont vous désirez la valeur des pluies cumulées")
print("(0 pour avoir tout le mois et -1 pour terminer)")
jour = eval(input("Jour ou période ? :"))
while jour != -1:
  affiche_valeur(pluies_septembre, jour)
  jour = eval(input("Jour ou période ? :"))
print("Au revoir et merci ! ")


