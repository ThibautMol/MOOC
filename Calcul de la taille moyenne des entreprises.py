"""Calcul de la taille moyenne des entreprises
    l'Input prend la valeur du nombre de salariés par entreprises
    La valeur -1 sera utilisée en input pour déclencher le break de la boucle et terminer l'input"""

user_input = 0
total_employees = 0
number_of_companies = 0

while True:
    user_input = int(input())
    
    if user_input == -1:
        break
    else:
        number_of_companies += 1
        total_employees += user_input

print(total_employees / float(number_of_companies ))