numMes = int(input("Ingrese un número de mes: "))

if numMes > 0 and numMes < 13 :
    #calculo el mes
    if numMes == 1 :
        cartel = "Enero"
    else :
        if numMes == 2 :
            cartel = "Febrero"
        else :
            if numMes == 3 :
                cartel = "Marzo"
            else :
                if numMes == 4 :
                    cartel = "Abril"
                else :
                    if numMes == 5 :
                        cartel = "Mayo"
                    else :
                        if numMes == 6 :
                            cartel = "Junio"
                        else :
                            if numMes == 7 :
                                cartel = "Julio"
                            else :
                                if numMes == 8 :
                                    cartel = "Agosto"
                                else :
                                    if numMes == 9 :
                                        cartel = "Septiembre"
                                    else :
                                        if numMes == 10 :
                                            cartel = "Octubre"
                                        else :
                                            if numMes == 11 :
                                                cartel = "Noviembre"
                                            else :
                                                if numMes == 12 :
                                                    cartel = "Diciembre"
    
else :
    cartel = "El número de mes es inválido"
    
print(cartel)
    

    
