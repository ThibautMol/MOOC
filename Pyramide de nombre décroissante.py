"""Pyramide de nombre décroissant à partir de son centre"""

n = int(input())

for i in range(1, n+1):
  # On calcule le nombre d'espaces à imprimer avant de commencer la ligne
  spaces = " " * (n - i)
  # On calcule les chiffres à imprimer dans la ligne
  digits = ""
  for j in range(i):
    digits += str((i + j) % 10)
  # On imprime la ligne en ajoutant les espaces et en répétant les chiffres de manière symétrique
  print(spaces + digits + digits[::-1][1:])