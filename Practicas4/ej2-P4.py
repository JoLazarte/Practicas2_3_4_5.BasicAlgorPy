#EPS+CC
# BANDERA: Variable que según su valor indica que es verdad que ocurre un suceso o no.

#Entrada:
nro=int(input("Ingrese nro: "))
#Proc:
#****inicializacion de variables:
par=True  # BANDERA, que cuando está en true significa que es par y cuando no, impar
ingresoAlgunNro=False #BANDERA, en verdadero cuando ingrese al menos un nro.

#***Fin de inicialización
while not (nro==-1):
    #subproceso:
        #En la primera vuelta, par es FALSE, en la segunda, es TRUE; tercera, FALSE, etc
    par=not par  # Esto es lo mismo que hacer:
    #if par :
    #    par=False
    #else:
    #    par=True
        
    ingresoAlgunNro=True #solo es TRUE si se ingresa algun num distinto de -1
    #Entrada:
    nro=int(input("Ingrese nro: "))
#Fin del Proc.
#Salida

if ingresoAlgunNro : #si sí se ingresaron números
    if par: 
        cartel="Es par"
    else:
        cartel="Es impar"
else:
    cartel="No ingreso nros"
print (cartel)

    