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
###-----------------------NIVEL BÁSICO-----------------------#####

day= int(input("Ingrese un día en números: "))
month= int(input("Ingrese un mes en números: "))
year= int(input("Ingrese un año en números: "))

fecha=False
    #rango de años válidos:
if(year>1580 and year<2030):
        #mes de febrero:
    if(month == 2):
            #¿es bisiesto?
        if((((year % 4 == 0) and not(year % 100 == 0)) or (year % 400 == 0)) and (day > 0 and day<30)):
            fecha=True
            #no es bisiesto:
        elif(day > 0 and day <29):
            fecha=True
        #resto de los meses:
    elif(month == 1 or (month > 2 and month < 13)):
            #meses de 31 días:
        if((day>0 and day<32)and(month !=2 and month != 4 and month != 6 and month != 9 and  month != 11)):
            fecha=True           
            #meses de 30 días:
        elif((day>0 and day<31)and(month == 4 or month == 6 or month == 9 or  month == 11)):
            fecha=True

print(fecha)

addDays=int(input("Ingrese un número para sumar al día actual: "))

if(fecha):
    for i in range(addDays):
        if((day>0 and day<31)and(month !=2 and month != 4 and month != 6 and month != 9 and  month != 11)):
            day=day+1
           
        else:
            if((day>0 and day<30)and(month == 4 or month == 6 or month == 9 or  month == 11)):
                day=day+1
                
            else:
                if((day>0 and day<28)and(month == 2)):
                    day=day+1
                        
                else:
                    if((day>0 and day<29)and(month == 2) and (((year % 4 == 0) and not(year % 100 == 0)) or (year % 400 == 0))):
                        day=day+1
                         
                    else:
                        if((day==31 or day == 30) and (month != 12)):
                            day=1
                            month=month+1
                              
                        else:
                            if(day==31 and month == 12):
                                day=1
                                month=1
                                year=year+1
                                   
                            else:
                                if((day==28) and month == 2):
                                    day=1
                                    month=3
                                      
                                else:
                                    if((day==29) and (month == 2) and (((year % 4 == 0) and not(year % 100 == 0)) or (year % 400 == 0))):
                                        day=1
                                        month=3
                                     
        
    
    print("Nueva fecha: ", day, month, year)