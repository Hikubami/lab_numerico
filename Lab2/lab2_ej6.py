from lab2ej5 import ripf  #Importo el ejercicio 5 del lab. 

hx  = ripf(lambda x : 2**(x-1), 1.5, 1e-5, 100) #Uso una función lambda pero también puede ir en una variable 

print(hx)