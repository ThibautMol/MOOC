"""Lecture température en input
    print différents textes selon la température entrée"""

temperature=int(input())
if temperature > 0 and temperature <= 10 :
    print("Il va faire frais.")
elif temperature <= 0 :
    print("Il va faire froid.")