#Entrada
n=int(input("Ingrese una cantidad N de alumnos: "))
#legajo=int(input("Ingrese un número de legajo: "))
#nota=int(input("Ingrese una nota: "))

#Proceso C.E.
#Inicialización
c = 1
sum = 0
legPares = 0
cantPromoc = 0
cantAprob = 0
#cantDesaprob = 0
cantTotal = 0

for c in range (1, n+1):
    
    legajo=int(input("Ingrese un número de legajo: "))
    
    cantTotal = cantTotal + 1
    
    #subprocesos
    #Ingresar y validar nota
    nota=int(input("Ingrese una nota: "))

    while (nota < 1 or nota > 10):
        #si la nota no es valida, la pido de nuevo
        nota=int(input("Ingrese una nota válida, entre el 1 y el 10: "))
    #fin de entrar y validar nota
    
    #procionado, aprobado, desaprobado, situación legajo
    if (nota >= 7):
        cantPromoc = cantPromoc + 1
        print("legajo: ", legajo, "promocionado")
        
    else:
        if (nota >= 4):
            cantAprob = cantAprob + 1
            print("legajo: ", legajo, "aprobado")
            
        else:
            cantDesaprob = cantTotal - (cantAprob+cantPromoc)
            print("legajo: ", legajo, "desaprobado")
    
    #nota máxima, nota mínima:
    if (c == 1):
        notaMax = nota
        legMax = legajo
        notaMin = nota
        
    else:
        if(notaMax < nota):
            notaMax = nota
            legMax = legajo
            
        else:
            if(notaMin > nota):
                notaMin = nota
    
    #promedio
    sum = sum + nota
    promedio = sum/cantTotal
    
    #legajos pares
    if legajo % 2 == 0 :
        legPares = legPares + 1
        
#Fin del proceso C.E.

#Salida
if cantTotal > 0:
    porcentajePromoc=cantPromoc/cantTotal*100
    porcentajeAprob=cantAprob/cantTotal*100
    
    print("Cantidad de aprobados", cantAprob)
    print("Cantidad de desaprobados", cantDesaprob )
    print("Porcentaje de promocionados", porcentajePromoc)
    print("Porcentaje de aprobados", porcentajeAprob)
    print("Promedio de notas", promedio)
    print("La nota máx es: ", notaMax)
    print("La nota mín es: ", notaMin)
    print("Cantidad de legajos pares: ", legPares)
else:
    print("No se ingresaron legajos")


