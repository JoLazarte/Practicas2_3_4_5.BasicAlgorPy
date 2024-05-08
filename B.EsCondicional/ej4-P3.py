nota1 = int(input("Ingrese la nota del primer parcial: "))
nota2 = int(input("Ingrese la nota del segundo parcial: "))


if (nota1 >= 0 and nota1 <= 10) and (nota2 >= 0 and nota2 <= 10) :
    if nota1 >= 7 and nota2 >= 7:
        cartel = "Promocionó"
    else :
        if nota1 >= 4 and nota2 >= 4:
            cartel = "Aprobó"        
        else :
            if nota1 <= 4 or nota2 <= 4:
                cartel = "Recupera"
                
else :
    cartel = "Alguna de las notas es inválida"

print(cartel)
