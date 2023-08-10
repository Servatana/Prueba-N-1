"""Numero1 = int(input("Inserte numero:"))
Numero2 = int(input("Inserte numero:"))

while Numero1==Numero2:
    if Numero1>Numero2:
        print(Numero1)
    elif Numero1<Numero2:
        print(Numero2)"""


Numero1=int(input("insertar un numero:"))
Numero2=int(input("insertar un numero:"))

while True:
    if Numero1>Numero2:
        print(Numero1)
        Numero1=Numero1
    elif Numero1<Numero2:
        print(Numero2)
        Numero1=Numero2
    Numero2=int(input("insertar un numero:"))



#Prueba para GitHub.