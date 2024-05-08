#precio de un viaje a partir de
#la cantidad de kilómetros que desea recorrer el usuario

#viajeMínimo = 250
#SOLO se cobra cuando el IMPORTE POR KM no alcanza este mínimo.

#Si recorre entre 0 y 10 km: $30 por km -> 10km * 30 = 300
#-> 250/30 = 8,333333333 km. A partir de los 8,4 km, ya no secobra
#Si recorre 10 km o más: $20 por km

kmTotales = float(input("Ingrese un número de km que desea recorrer: "))

if kmTotales > 0 and kmTotales < 8.4:
    costo = 250
    print("El costo total es: ", costo)
else:
    if kmTotales >= 8.4 and kmTotales < 10:
        costo = kmTotales * 30
        print("El costo total es: ", costo)
    else:
        if kmTotales >=10:
            costo = kmTotales * 20
            print("El costo total es: ", costo)
            
