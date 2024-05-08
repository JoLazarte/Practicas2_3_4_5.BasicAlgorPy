# Entrada de datos

TieneSolucion=input ("Con los datos de entrada, más los asumidos, más los conocidos, es posible obtener los datos de salida? (s/n)")



# Proceso

if TieneSolucion=="s":
    cartel="Utilice esquema E-P-S "
    TieneRepeticiones=input ("¿Hay acciones que se repiten? (s/n)")
    if TieneRepeticiones=="s":
        ConoceLaCantidadDeRepeticiones=input ("¿Conoce las acciones que se repiten antes de que se repitan? (s/n)")
        if ConoceLaCantidadDeRepeticiones=="s":
            cartel+=" con Esquema CICLO EXACTO (C.E)"
        else :
            cartel+=" con Esquema CICLO CONDICIONAL (C.C)"                
else:
    cartel="No tiene solucion "

    
# Salida

print (cartel)



