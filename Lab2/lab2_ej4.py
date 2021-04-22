from lab2_ej3 import rnewton 


def raiz_a(a):
    assert(a>0)
    def fun(x):
        return (x**3-a, 3*(x**2))
    hx,hy=rnewton(fun,a-1,1e-6,100)
    print(hx,'\n',hy)

raiz_a(8)