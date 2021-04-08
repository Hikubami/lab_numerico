import math
import random

# input_1= int(input("Ingrese el primer valor:"))
# input_2= 1 / int(input("Ingrese el segundo valor (1/y): "))


def SonReciprocos(first,second):
    if (first*second == 1):
        return True

    else:
        return False




for _ in range(100):
    x = 1 + random.random()
    y = 1/x
    if not SonReciprocos(x,y):
        print(x)

