"""
Programa: ingresar la terminación de la patente (entre 0 y 9) hasta ingresar -1 
Cuántos autos con patente par y cuántos autos con patente impar hay en un día
"""
#Entrada
numFinPatente = int(input("Ingrese nro final de la patente: "))
sumPar = 0
sumImpar = 0
c=1
#Proceso C.C.
while numFinPatente != -1:
    
    while (numFinPatente<=0 or numFinPatente>9):
        numFinPatente = int(input("El nro debe ser mayor a 0 y menor a 9. Ingrese nro final de la patente nuevamente: "))
        
    if (numFinPatente%2==0):
        sumPar = sumPar + 1
    else:
        sumImpar = sumImpar + 1
    numFinPatente = int(input("Ingrese nro final de la patente: "))

    c=c+1
    
print(sumPar)
print(sumImpar)