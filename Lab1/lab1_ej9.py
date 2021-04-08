
def horn(coefs, x0):

    n = len(coefs)
    b = coefs[0]
    for index in range(1,n):
        b = coefs[index] + b * x0

    return b

j=horn([2,2,3,-21,8],8)
print(j)