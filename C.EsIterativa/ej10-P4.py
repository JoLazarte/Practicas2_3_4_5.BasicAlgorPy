"""
Factorial de un número entero N > 0 = el producto de todos los enteros X tales que 0 < X <= N.
Desarrollar un programa para calcular el factorial de un número dado. Deberán rechazarse las entradas inválidas (menores que 0).
 " N ! "
"""
# EPS+CE

#Entrada
n=int(input("Ingrese nro de termino: "))

#inicializacion
Factorial=1 #porque 1 es el primer num entero mayor a 0

#Proc: 
for c in range(2,n+1): #ya inicializamos a Factorial como 1, no queremos multiplicar 1 x 1, sino 1 x 2 => emepzamos el bucle con 2
    #Subproceso:
    Factorial*=c
    #print(Factorial)
#Salida:
if n > 0: #Ya esta definido en el bucle for que solo se aceptan num a partir del 2...
    print ("El factorial de ",  n, "es ", Factorial)
else:
    print ("El nro debe ser mayor a 0")  

