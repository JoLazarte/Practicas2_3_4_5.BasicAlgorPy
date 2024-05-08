"""
Ingresar números hasta que la suma de los números pares supere 100.
Mostrar cuántos números se ingresaron en total.
"""
#Entrada

c=0
sumPar=0


#Proceso C.C.
while (sumPar < 100):
    nro=int(input("Ingrese nro: "))
    
    c=c+1 #cuántas vueltas se dieron?
    
    if (nro%2==0):
        sumPar = sumPar + nro


#Salida
print(c)