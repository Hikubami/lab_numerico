import math
import matplotlib.pyplot as plt


#Actividad 1: Método de la Secante 
def rsecante(fun,x0,x1,err,mit):
    f = (fun(x1) - fun(x0)) / (x1-x0)

    hx,hf = [x0], [f]
    
    
    k = 0
    
    for k in range(mit):
        xn = x1 - fun(x1)*((x1-x0)/(fun(x1)-fun(x0)))

        if abs((xn-x0)/xn) < err:
            print('El paso es muy pequeño')
            return hx, hf, k

        x0 = x1
        x1 = xn
        f = fun(x0)
        hx.append(x1)
        hf.append(f)


        k += 1
    return hx,hf,k


#Método de Newton 
def rnewton(fun, x0, err, mit):
    f, df = fun(x0)

    hx, hf = [x0], [f]

    if df == 0:
        print('La derivada es nula en tal punto')
        return hx, hf, k

    
    k = 0

    while (abs(f) >=err) and (k < mit):
    
        xn = x0 - f/df
    
        if abs( (xn - x0)/xn ) < err:
            print('El paso es muy pequeño')
            return hx, hf, k

        x0 = xn
        f, df = fun(x0)
        hx.append(x0)
        hf.append(f)
        
        k +=1

    return hx, hf, k



#ACTIVIDAD 2: 
def busqueda_ceros(fun, x0, x1, err, mit):


    def solo_primero(x):
        first, tr = fun(x) 
        return first

    sec_x,sec_it,it1=rsecante(solo_primero,x0,x1,err,mit)
    print('Metodo de la Secante \nEl cero es:',sec_x[it1],'\nLas iteraciones:',it1, '\n\n')
    
    new_x,new_it,it2=rnewton(fun,x0,err,mit)
    print('Metodo de Newton \nEl cero es:',new_x[it2],'\nLas iteraciones:',it2,'\n\n')

    sec_value=solo_primero(sec_x[it1])
    new_value=solo_primero(new_x[it2])

    if abs(sec_value)<abs(new_value):
        return sec_x[it1]     
    else:
        return new_x[it2]

#Función auxiliar para busqueda_ceros
def funcion_polinomio(x):
    return (x**3+x-5, 3*(x**2)+1)


#ACTIVIDAD 3: Algoritmo de Horner
def horn(coefs, x0):

    n = len(coefs)
    result = coefs[0]
    for index in range(1,n):
        result = coefs[index] + result * x0

    return result

#Llamadas y evaluaciones:
mejor_cero = busqueda_ceros(funcion_polinomio,10,-10,1e-6,15)
print('El mejor cero es:', mejor_cero, '\n\n')

polinomio = horn([1,0,1,-5],mejor_cero) #El Polinomio es: x³+x-5 == [1,0,1,-5], mejor_cero
polinomio2 = (horn([3,0,1],mejor_cero)) #La Derivada es: 3x²+1 == [3,0,1]

print('Polinomio es:',polinomio,'Donde polino es horner evaluado en mejor Cero')
print('Polinomio2 es:',polinomio2,'Donde polino2 es horner derivado evaluado en mejor Cero')


#ACTIVIDAD 4: Gráfico
#Comienzo con la función
def funcion_aux(x):
    return (x**3)+x-5

#Primero Establezco las listas para enfrentar al gráfico:
x=[-2,-1,0,1,2,3,4]
y=[funcion_aux(x_i) for x_i in x]

#Continuo con la llamada del método más cercano:
#o=======================o WARNING o======================o 
# REVISA POR FAVOR PORQUE EL INTERVALO USADO ES [-2,4]
# Y TENGO LA DUDA DE SI TIENE QUE SER ESE O [-10,10]
lx,lf,it = rsecante(funcion_aux,4,-2,1e-6,15)

#Parte para graficar
plt.title("Polinomio y Método de la Secante")
plt.plot(lx,lf,"red",label="Secante")
plt.plot(x,y,label="Polinomio")
plt.legend()
plt.show()