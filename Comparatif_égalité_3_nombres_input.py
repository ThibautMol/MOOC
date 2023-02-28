"""Comparatif 3 nombres input"""


def deux_egaux(a ,b, c) :
    if a == b or a == c or b == c :
        result = True
    else :
        result = False
    return result
a=input("entrez la valeur de a :")
b=input("entrez la valeur de b :")
c=input("entrez la valeur de c :")

result=deux_egaux(a, b, c)
print(result)