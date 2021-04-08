#Actividad 7

x = int(input("ingrese la base debe ser numero real: "))
assert(type(x) is int)
n = int(input("ingrese la potencia: "))

def potencia(base,potencia):
    i=1
    result = base
    while i < potencia:
        result = result*base
        i = i+1
    print("El resultado de",base,"elevado a",potencia,"es",result)

potencia(x,n)

it = 0
while it < 5:
    potencia(x,it+1)
    it = it+1
