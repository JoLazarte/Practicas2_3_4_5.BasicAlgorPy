"""
Escribir una función que reciba como parámetros un número de día, un número
de mes y un número de año y devuelva la cantidad de días que faltan hasta fin
de mes. Luego desarrollar tres programas para:
· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
la cantidad de días que faltan hasta fin de año.
· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
la cantidad de días transcurridos en ese año hasta esa fecha.
· Ingresar dos fechas formadas por tres enteros (día, mes y año) e imprimir
cuánto tiempo transcurrió entre ambas, expresando el resultado en
años, meses y días.
Los tres programas deben realizar su trabajo a través de la función indicada al
comienzo.


"""


def bisiesto(anio):
    bisiesto=False
    if anio % 4 ==0:
        if anio % 100 ==0:
            if anio % 400==0:
                bisiesto=True
        else:
            bisiesto=True
    return bisiesto


        
def diasRestantesDelMes(mes, dia,anio=2021):
    if mes!=2:
        dias=30
        if (mes > 7 and mes % 2==0) or (mes <= 7 and mes % 2==1):
                dias=31       
    else:
        if(bisiesto(anio)):
            dias=29
        else:
            dias=28
    return dias - dia   


def mesSiguiente(mes):
    
    if mes==12:
        mes=1
    else:
        mes+=1
       
    return mes   


def DiasEntreFechas(diai,mesi,anioi, diaf,mesf,aniof):
    dias=0
    while (diai !=diaf or mesi !=mesf or anioi != aniof):
        if (mesi==mesf and anioi==aniof):
            dias=dias +diaf-diai
            diai=diaf
        else:
            dias=dias+diasRestantesDelMes(mesi, diai,anioi) +1
            mesi=mesSiguiente(mesi)
            if mesi == 1:
               anioi+=1
            diai=1   
    return dias    
#Salida                

def diferenciaEntreFechasDiasMesAnio (diai,mesi,anioi, diaf,mesf,aniof):
    # P lo subdivido en  mes, dia, año
    # dia
    if diaf >=diai:  
        dia=diaf-diai
    else:
        dia=diasDelMes(mesi,anioi)-diai +diaf
        mesi=mesSiguiente(mesi) # paso al mes siguiente
        if mesi == 1:
            anioi+=1  
# mes
    if mesf >=mesi:  
        mes=mesf-mesi
    else:
        mes=12-mesi +mesf
        anioi+=1 # paso al año siguiente

#anio
    anio=aniof-anioi
#Fin Proc
#Salida
    return str(dia)+"/"+str(mes)+"/"+str(anio)

       

print ("")
print ("Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir")
print ("a cantidad de días que faltan hasta fin de año.")
print ("")

#· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
## la cantidad de días que faltan hasta fin de año.
diai=int(input("Ingrese dia:"))
mesi=int(input("Ingrese mes:"))
anioi=int(input("Ingrese anio:"))

diaf=31
mesf=12
aniof=anioi
#Proceso

print("Dias transcurridos:", DiasEntreFechas(diai,mesi,anioi, diaf,mesf,aniof))         
print ("")
print ("Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir")
print ("la cantidad de días transcurridos en ese año hasta esa fecha.")
print ("")
#Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
#la cantidad de días transcurridos en ese año hasta esa fecha.
diaf=int(input("Ingrese dia:"))
mesf=int(input("Ingrese mes:"))
aniof=int(input("Ingrese anio:"))

diai=1
mesi=1
anioi=aniof
#Proceso

print("Dias transcurridos:", DiasEntreFechas(diai,mesi,anioi, diaf,mesf,aniof)) 
print ("")        
print ("Ingresar dos fechas formadas por tres enteros (día, mes y año) e imprimir cuánto tiempo transcurrió entre ambas")
print (", expresando el resultado en años, meses y días")
print ("")

    
diai=int(input("Ingrese dia:"))
mesi=int(input("Ingrese mes:"))
anioi=int(input("Ingrese anio:"))

diaf=int(input("Ingrese dia:"))
mesf=int(input("Ingrese mes:"))
aniof=int(input("Ingrese anio:"))

print(diferenciaEntreFechasDiasMesAnio (diai,mesi,anioi, diaf,mesf,aniof))
          