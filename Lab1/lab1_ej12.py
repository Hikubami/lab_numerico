import math

def sonOrtogonales(x,y): 
    cal = (x[0]*y[0]) + (x[1]*y[1])
    if cal == 0:
        print("Son ortogonales")
        return True
    else:
        print("No son ortogonales")
        return False
    
x = [1, 1.1024074512658109]
y = [-1, 1/x[1]]

if not sonOrtogonales(x,y):
    print("Algo salió mal")


"""
Lo que sucede es que y[1] está multiplicandose
y dividiendo por x[1] pero como resultado da 0.9 periódico
"""

