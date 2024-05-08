"""
CONDICIONAL: Leer tres números correspondientes al día, mes y año de una fecha e imprimir
un mensaje indicando si la fecha es válida o no.
"""

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