print("Quelle operation voulez vous faire?")
print("1 : +")
print("2 : -")
print("3 : *")
print("4 : /")

op = int(input("Selection: "))
on = True

if op == 1:
    on = "+"
elif op == 2:
    on = "-"
elif op == 3:
    on = "*"
elif op == 4:
    on = "/"
else:
    on = True
    print("Cette selection n'est pas valide!")


def rr():
    print("Votre resultat est de {0}.".format(r))


if on in ["+","-","*","/"]:
    n1 = float(input("choisissez le premier nombre: "))
    n2 = float(input("choisissez le deuxième nombre: "))
    if on == "+":
        r = n1 + n2
        rr()
    elif on == "-":
        r = n1 - n2
        rr()
    elif on == "*":
        r = n1 * n2
        rr()
    elif on == "/":
        r = n1 / n2
        rr() 
input()           