"""exemples de manipulations de listes"""
t=(1,2,3,4,5,6,9)
s=list(t)
u={4,5,7,9}
v=tuple(u)
x=list(t)
w=str(t)

print("contenue de s:",s)
print("contenue de t:",t)
print("contenue de u:",u)
print("contenue de v:",v)
print("contenue de x:",x)
print("contenue de w:",w)

print("type de s:",type(s))
print("type de t:",type(t))
print("type de u:",type(u))
print("type de v:",type(v))
print("type de x:",type(x))
print("type de W:",type(w))

def foo(liste):
    return [liste, liste]

x = [2,3]
x = foo(x)
print(x) #on aura deux listes dans une liste.


def foo(liste):
    return liste + liste

x = [2,3]
x = foo(x)
print(x) #on aura une seule liste avec deux fois les éléments