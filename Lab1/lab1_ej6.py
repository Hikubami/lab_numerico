#Actividad 6

def es_mayor(primero,segundo):
    if primero > segundo:
        print("El número",primero,"es mayor")

    if segundo > primero:
        print("El número",segundo,"es mayor")
    
    if primero == segundo:
        print("Ambos son iguales")

first = int(input("Ingresa el primer número: "))
second = int(input("Ingresa el segundo número: "))

assert(type(first) is int)
assert(type(second) is int)

es_mayor(first, second)