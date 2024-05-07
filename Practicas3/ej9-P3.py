#calcule y muestre el sueldo neto de un empleado 
#en base a su sueldo básico y su antigüedad en años.
#Si es soltero: + 5% del salario bruto por cada año de antigüedad, 5 * suelBas / 100
#Si es casado: + 7% del salario bruto por cada año de antigüedad, 7 * suelBas / 100
#Descuentos: Jubilación: -11%, Obra Social: -3%, Sindicato: -3%

suelBas = float(input("Ingrese su salario básico en números: "))
antig = float(input("Ingrese sus años de antigüedad en números: "))

estCivil = int(input("Ingrese su estado civil con un número: 1. Soltero, 2. Casado "))

#Descuentos: 
jubilac = 11 * suelBas / 100
obraSoc = 3 * suelBas / 100
sindic = obraSoc #3 * suelBas / 100

#Estado civíl:
if estCivil == 1:
    
    suelNeto = suelBas + antig * (5 * suelBas / 100) - jubilac - obraSoc - sindic
    print(suelNeto)
    
else:
    if estCivil == 2:
    
        suelNeto = suelBas + antig * (7 * suelBas / 100) - jubilac - obraSoc - sindic
        print(suelNeto)
    
    else:
        cartel = "Opción de estado civil incorrecta"
        print(cartel)
        