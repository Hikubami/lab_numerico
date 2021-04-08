import math
import sys

print("¿Qué función desea usar? Buena o Mala")
print("[1] Bhaskara (Mala)")
print("[2] Función Buena")
option = int(input("Ingrese 1 o 2: "))

if (option != 1) & (option != 2):
    print("Valor incorrecto")
    print("Terminando programa...")
    sys.exit()

cuadrado= int(input("Ingrese coeficiente de x²: "))
simple= int(input("Ingrese coeficiente de x: "))
independiente= int(input("Ingrese valor independiente: "))

def mala(a,b,c):
    x1= (-b+math.sqrt((b**2)-4*a*c))/(2*a)
    x2= (-b-math.sqrt((b**2)-4*a*c))/(2*a)
    return [x1,x2]


def buena(a,b,c):
    if b >= 0:
        x_1= (-b-math.sqrt((b**2)-4*a*c))/2*a
    else:
        x_1= (-b+math.sqrt((b**2)-4*a*c))/2*a

    x_2= c/(a*x_1)

    return [x_2,x_1]

if(option == 1):
    [raiz_1,raiz_2]= mala(cuadrado,simple,independiente)
    print("Las raíces calculadas con la función mala es:",[raiz_1,raiz_2])

if(option == 2):
    [raiz_1,raiz_2]= buena(cuadrado,simple,independiente)
    print("Las raíces calculadas con la función buena es:",[raiz_1,raiz_2])
