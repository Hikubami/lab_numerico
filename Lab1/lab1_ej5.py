#Actividad 5

def factorial_de(number):
    total=1

    if number > 1:
        base=number 
        while base > 1:
            total *= base
            base -= 1

    print("El factorial de",number,"es:",total)

#5a)Factorial de 6
x=6
factorial_de(x)

#5b) Función de libreria math
from math import factorial
y=factorial(x)
print("Factorial con función de la libreria math de 6 es:",y)

#5c) Calculo de los factoriales de numero n dado por el usuario
numero_input=int(input("Ingrese un número: "))
factorial_de(numero_input)
