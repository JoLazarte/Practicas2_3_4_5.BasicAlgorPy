

print ("Bienvenido")
totalAprobados = 0
totalReprobados = 0
totalAplazados = 0

nro = 0
auxVerificacion = 0
print ("Por Favor, ingrese Legajo del Alumno/a; ingrese -1 para terminar")

while not (nro==-1):
    nro=int(input("Ingrese Legajo del alumno=>"))
    while (1>nro and nro<10):
        if (auxVerificacion == 1):
            print ("Por Favor, ingrese un numero del 1 al 10")
            auxVerificacion = 0
        nro=int(input("Ingrese la Nota del alumno=>"))
        auxVerificacion = 1
    auxVerificacion = 0
    if nro==1:
        totalAplazados +=1
        totalReprobados +=1
        print("No Aprobo")
    elif nro<5:
        totalReprobados +=1
        print("No Aprobo")
    else:
        totalAprobados +=1
        print("Aprobo")
    

print("Alumnos Aprobados",totalAprobados)
print("Alumnos Reprobados",totalReprobados)
procentajeAplazos = totalAplazados * 100 / (totalAprobados + totalReprobados + totalAplazados)
print("Alumnos Aplazados",procentajeAplazos,'%')
