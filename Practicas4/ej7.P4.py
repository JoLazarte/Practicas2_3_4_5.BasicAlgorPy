"""
Leer 10 números enteros e imprimir su promedio, el mayor valor leído y en qué
posición se encontraba. Si se ingresó más de una vez sólo debe informar la primera.
"""
#Entrada

sum=0
c=1
posMax=0
#Proceso C. E.

for c in range (1,11):
    nro=int(input("Ingrese nro: ")) #se ingresará unas 10 veces
    sum=sum+nro
   
    if (c == 1): #primera vuelta
        max = nro
        posMax = c

    else: #segunda y siguientes vueltas
        if (max<nro):
            max = nro
            posMax = c
    #No necesito incrementar c, porque en el ciclo FOR el nro de vueltas ya está definido.
    
#Salida
if (c>0):
    prom=sum/c
    print(prom)
    
    print(max)
    print(posMax)        
