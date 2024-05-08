numYear = int(input("Ingrese un año en números: "))

if (numYear % 4 == 0 and numYear % 100 > 0) or (numYear % 4 == 0 and numYear % 100 == 0 and numYear % 400 == 0):
    cartel = "Es un año bisiesto"
    print(cartel)
    
else:
    cartel = "El año no es bisiesto"
    print(cartel)
   