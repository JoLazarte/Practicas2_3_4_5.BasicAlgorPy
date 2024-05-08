#Entrada
nro=int(input("Ingrese nro: "))

#Inicializar acumuladores/contador para max y min:
c=1

#inicializo el sumador para el promedio:
sum=0

while nro != -1:
    
    #subproceso
    #maximos y minimos
    if (c == 1): #primera vuelta
        max = nro
        min = nro
        #c= c+1
    else:         #siguiente vuelta, siguientess vueltass...
        if (max<nro):
            max = nro #nuevo num/máximo comparado con el anterior
        if (min>nro): 
            min = nro  #nuevo num/mínimo comparado con el anterior
    
    c=c+1

    #suma
    sum = sum + nro
    #fin del subproceso
            
    nro=int(input("Ingrese nro: "))
#fin del while

#salida
    
#promedio
prom = sum / (c-1)

if c > 0:
    
    print("El máx es: ", max)
    print("El mín es: ", min)
    print("El valor de la suma es: ", sum)
    print("El promedio es: ", prom)
    
else:
    print("No ha ingresado nros ")

    
