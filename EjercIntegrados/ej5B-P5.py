"""
-----------------------------------------------------------------------------------------------
Título: DÍA SIGUIENTE

Fecha: 28/08/23

Autor:

Descripción:

NIVEL BÁSICO: Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y
un número entero N que representa una cantidad de días. Realizar un programa que imprima
la nueva fecha que resulta de sumar N días a la fecha dada.
Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 7 de la práctica 3.

NIVEL INTERMEDIO: Escribir una función diaSiguiente(…) que reciba como parámetro una fecha cualquiera expresada
por tres enteros (correspondientes al día, mes y año) y calcule y devuelva tres enteros correspondientes al día siguiente al dado.
Utilizando esta función, desarrollar programas que permitan:
        A. Sumar N días a una fecha.
        B. Calcular la cantidad de días existentes entre dos fechas cualesquiera.

Pendientes: Considerar que meses tienen 30 días y cuales solo 30, además de cuando hay año bisciesto.

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def bisiesto(yearBis):
    bisiesto=False
    if yearBis % 4 ==0:
        if yearBis % 100 ==0:
            if yearBis % 400==0:
                bisiesto=True
        else:
            bisiesto=True

    return bisiesto

def nonEvenMonth(currentMonth):
    evenMonth=False
    if(currentMonth == 1 or (currentMonth > 2 and currentMonth < 13)): 
        #meses de 31 días:
        if((currentMonth > 7 and currentMonth % 2==0) or (currentMonth <= 7 and currentMonth % 2==1)):
            evenMonth=True  
    return evenMonth
           

def validDate(day, month, year):
   
    fecha=False
    #rango de años válidos:
    if(year>1580 and year<2030):
        #mes de febrero:
        if(month == 2):
            #Bisiesto
            if((bisiesto(year)==True and (day>0 and day<30)) or (bisiesto(year)==False and (day>0 and day<29))):
                fecha=True        
        #resto de los meses:
        elif((nonEvenMonth(month)==True and (day>0 and day<32)) or (nonEvenMonth(month)==False and (day>0 and day<31))):
            fecha=True        
                        
    return fecha

def diaSiguiente(day, month, year):
    
    valid=validDate(day, month, year)
    fecha=[]
    if(valid==True):

        if(month==2):
            if(bisiesto(year)==False):
                if(day==28):
                    day=1
                    month=3
                    fecha=[day, month, year]
                    print("La fecha del día siguiente es: ", fecha)    
                elif(day<28):
                    day=day+1
                    fecha=[day, month, year]
                    print("La fecha del día siguiente es: ", fecha)
            elif(bisiesto(year)==True):
                if(day==29):
                    day=1
                    month=3
                    fecha=[day, month, year]
                    print("La fecha del día siguiente es: ", fecha)    
                elif(day<29):
                    day=day+1
                    fecha=[day, month, year]
                    print("La fecha del día siguiente es: ", fecha)

        elif(month!=2):
            if(month!=12):
                if(nonEvenMonth(month)==True):
                    if(day==31):  
                        day=1
                        month=month+1
                        fecha=[day, month, year]
                        print("La fecha del día siguiente es: ", fecha)
                    elif(day<31):
                        day=day+1
                        fecha=[day, month, year]
                        print("La fecha del día siguiente es: ", fecha)
                if(nonEvenMonth(month)==False):
                    if(day==30):  
                        day=1
                        month=month+1
                        fecha=[day, month, year]
                        print("La fecha del día siguiente es: ", fecha)
                    elif(day<30):
                        day=day+1
                        fecha=[day, month, year]
                        print("La fecha del día siguiente es: ", fecha)
            elif(month == 12):
                if(day==31):
                    day=1
                    month=1
                    year=year+1
                    fecha=[day, month, year]
                    print("La fecha del día siguiente es: ", fecha)
                elif(day<31):
                    day=day+1
                    fecha=[day, month, year]
                    print("La fecha del día siguiente es: ", fecha)
                 
    else:
        print("Fecha inválida")
        
    
    return fecha
            
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#-------------------------------------------------
thisDay= int(input("Ingrese un día en números: "))
thisMonth= int(input("Ingrese un mes en números: "))
thisYear= int(input("Ingrese un año en números: "))

#-------------------------------------------------
# Procesos
#-------------------------------------------------
valid2=validDate(thisDay, thisMonth, thisYear)
diaSiguiente(thisDay, thisMonth, thisYear)
print()
#Agregar N días a una fecha:

if(valid2==True):
    daysAdded=int(input("Ingrese un número para sumar al día actual: "))
    # La técnica es agregarle a la fecha ingresada 1 día tantas veces como lo indique diasAgregados
    for i in range(daysAdded):
        thisDay, thisMonth, thisYear = diaSiguiente(thisDay, thisMonth, thisYear) # Aquí utilizo la técnica de desempaquetar una lista

    print()
    print("La nueva fecha es: ", thisDay, thisMonth, thisYear)

else:
    print("Fecha inválida. No se pueden agregar días a una fecha inválida.")
        
#Calcular cant de días entre dos fechas:  
otherDay= int(input("Ingrese otro día en números: "))
otherMonth= int(input("Ingrese otro mes en números: "))
otherYear= int(input("Ingrese otro año en números: "))
valid3=validDate(otherDay, otherMonth, otherYear)
c=0
if(valid2 and valid3):
    
    if(thisYear==otherYear):
        if(thisMonth==otherMonth):
            while(thisDay !=otherDay):
                if(thisDay < otherDay):
                    thisDay, thisMonth, thisYear = diaSiguiente(thisDay, thisMonth, thisYear)
                
                elif(thisDay > otherDay):
                    otherDay, otherMonth, otherYear = diaSiguiente(otherDay, otherMonth, otherYear)
                
                c=c+1
        elif(thisMonth<otherMonth):
            while(thisDay !=otherDay or thisMonth !=otherMonth):
                thisDay, thisMonth, thisYear = diaSiguiente(thisDay, thisMonth, thisYear)
                c=c+1
        elif(thisMonth>otherMonth):
            while(thisDay !=otherDay or thisMonth !=otherMonth):
                otherDay, otherMonth, otherYear = diaSiguiente(otherDay, otherMonth, otherYear)
                c=c+1
    elif(thisYear<otherYear):
        while(thisDay !=otherDay or thisMonth !=otherMonth or thisYear !=otherYear):
            thisDay, thisMonth, thisYear = diaSiguiente(thisDay, thisMonth, thisYear)
            c=c+1
    elif(thisYear>otherYear):
        while(thisDay !=otherDay or thisMonth !=otherMonth or thisYear !=otherYear):
            otherDay, otherMonth, otherYear = diaSiguiente(otherDay, otherMonth, otherYear)
            c=c+1       
    
    print("La cantidad de dias entre las fechas ingresadas es: ", c)

#-------------------------------------------------
# Resultados
#-------------------------------------------------










