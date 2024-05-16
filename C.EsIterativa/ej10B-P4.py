"""
Factorial de un número entero N > 0 = el producto de todos los enteros X tales que 0 < X <= N.
 N!
"""
def factorial(n):
    result=1
    for i in range (1, n+1):
        result=result*i
    return result


x=int(input("Ingrese nro: "))
print("el factorial es", factorial(x))
