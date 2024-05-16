"""
Factorial de un número entero N > 0 = el producto de todos los enteros X tales que 0 < X <= N.
Desarrollar un programa para calcular el factorial de un número dado. Deberán rechazarse las entradas inválidas (menores que 0).
 " N ! "
"""
# EPS+CE

#Entrada
n=int(input("Ingrese nro de termino: "))

#inicializacion
Factorial=1 #porque 1 es el primer num entero mayor a 0 y porque fact(0)=1 y fact(1)=1

#Proc: 
for c in range(1,n+1): #empezamos a calcular desde fact(1): 1 x 1 hasta fact(n): n * fact(n-1).
    #Subproceso:
    Factorial*=c
    #print(Factorial)
#Salida:
if n > 0: #Ya esta definido en el bucle for que solo se aceptan num a partir del 2...
    print ("El factorial de ",  n, "es ", Factorial)
else:
    print ("El nro debe ser mayor a 0")  

