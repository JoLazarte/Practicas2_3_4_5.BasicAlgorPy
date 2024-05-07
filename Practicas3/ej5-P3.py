#costoBasLibro=500
#encuadernacion-rusxpag= 3.20
#libroMas300pag-EncTela=200
#libroMas600pag-EncTela=336

numPag = int(input("Ingrese un número de páginas del libro: "))

if numPag > 0 and numPag <= 300:
    costoTotal = float(numPag * 3.20 + 500)
    print(costoTotal)
else:    
    if numPag > 300 and numPag <= 600:
        costoTotal = float(numPag * 3.20 + 500 + 200)
        print(costoTotal)
        
    else :
        if numPag > 600:
            costoTotal = float(numPag * 3.20 + 500 + 336)
            print(costoTotal)

    
    


