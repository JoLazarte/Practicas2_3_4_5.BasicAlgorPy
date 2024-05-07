"""
Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. ¿Cómo cambiaría el
algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?
"""
#Entrada
numAMult = 4
nroTbMx=int(input("Ingrese nro a multiplicar: "))

#Inicialización
c=1

#Proceso P. C.
for c in range (1,13):
    multip4 = c*numAMult
    print(multip4, end=", ")
print(" ")
for c in range (1,13):
    multip = c*nroTbMx
    print(multip, end=", ")

#Salida
#el usuario pueda decidir la tabla de multiplicar a mostrar
