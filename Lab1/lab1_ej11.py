import math

def funcion_f(x):
    m = math.sqrt((x**2) +1)-1
    return m

def funcion_g(x):
    m = (x**2)/(math.sqrt((x**2) +1)+1)
    return m

# input1 = int(input("Ingrese el x: "))

# output1= funcion_f(input1)
# output2= funcion_g(input1)

# print("El output de f(x) es", output1)
# print("El output de g(x) es", output2)

for i in range(20):
    x = 8**-i
    print(f"f(x)={funcion_f(x)}, g(x)={funcion_g(x)}")

""" 
Preguntas: 
¿Ambas funciones dan los mismos resultados?

No, si bien comparten los primeros dígitos pero los ultimos 
dígitos varían de acuerdo a la función. 

¿Cuál es más confiable?

La más confiable es g(x), ya que a partir de la décima iteración,
f(x) se vuelve 0 mientras que g(x) devuelve un resultado más cercano.

"""