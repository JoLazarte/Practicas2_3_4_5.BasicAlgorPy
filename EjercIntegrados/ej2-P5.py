"""
Ingresar los números de legajo de los alumnos de un curso y su nota de examen final.
El fin de la carga se determina ingresando un -1 en el legajo.
Informar para cada alumno si aprobó o no el examen: se aprueba con nota >= 4.
Validar que la nota ingresada sea entre 1 y 10.
Informar:
· Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
· Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
· Porcentaje de alumnos que están aplazados (tienen 1 en el examen).
"""
#Entrada
legajo=int(input("Ingrese legajo: "))
#nota=int(input(“Ingrese nota”))

#Proceso
#Inicialización:
cantAprobados=0
cantTotal=0
cantAplazados=0

while legajo != -1:
    #subproceso
    #Entrar y validar nota:
    nota=int(input("Ingrese nota: "))
    while (nota < 1 or nota > 10):
        #si la nota no es valida se la pido de nuevo
        nota=int(input("La nota debe ser mayor o igual a 1 y menor o igual que 10: "))
    #fin de entrar y validar nota
    if(nota>=4):
        cantAprobados+=1
    cantTotal+=1
    if(nota==1):
        cantAplazados+=1
        
    legajo=int(input("Ingrese legajo: "))
    


#Salida
if cantTotal > 0:
    porcentajeAplazados=cantAplazados/cantTotal*100
    cantDesaprobados=cantTotal-cantAprobados
    print("Cantidad de aprobados", cantAprobados)
    print("Cantidad de desaprobados", cantDesaprobados )
    print("Porcentaje de aplazados", porcentajeAplazados)
else:
    print("No se ingresaron notas")
