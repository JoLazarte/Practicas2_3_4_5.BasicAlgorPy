"""
-----------------------------------------------------------------------------------------------
Título: ejercicio 8
Fecha:
Autor:

Descripción: 
Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3).
Por cada empleado se lee su legajo, categoría y salario.
Elaborar un informe que contenga:
· Importe total de salarios pagados por la empresa.
· Cantidad de empleados que ganan más de $200000.
· Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3.
· Legajo del empleado que más gana.
· Sueldo más bajo.
· Importe total de sueldos por cada categoría.
· Salario promedio

Pendientes:


-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#-------------------------------------------------
legajoEmp = int(input("Ingrese el legajo del empleado: "))

sueldoMax = 0
sueldoMin = 0
legajoMax = 0
legajoMin = 0

impTotSalPagados = 0
empGananMas200000 = 0
empGanMen50000Cat3 = 0

impTotSueldoCat1 = 0
impTotSueldoCat2 = 0
impTotSueldoCat3 = 0
salarioProm = 0
c=0
#-------------------------------------------------
# Procesos
#-------------------------------------------------
while(legajoEmp !=-1):
    categoriaEmp = int(input("Ingrese una categoría en los números 1, 2 o 3: "))
    while(categoriaEmp<1 or categoriaEmp>3):
        categoriaEmp = int(input("Ingrese una categoría válida. Elija entre los números 1, 2 o 3: "))
    
    salarioEmp = int(input("Ingrese el salario del empleado: "))
    
    if(c==1):
        sueldoMax=salarioEmp
        legajoMax=legajoEmp
        sueldoMin=salarioEmp
        legajoMin=legajoEmp      
    elif(salarioEmp>sueldoMax):
        sueldoMax=salarioEmp
        legajoMax=legajoEmp
    elif(salarioEmp<sueldoMin):
        sueldoMin=salarioEmp
        legajoMin=legajoEmp
        
    if(categoriaEmp==1):
        impTotSueldoCat1 +=salarioEmp
    if(categoriaEmp==2):
        impTotSueldoCat2 +=salarioEmp
    if(categoriaEmp==3):
        impTotSueldoCat3 +=salarioEmp
        
    impTotSalPagados = impTotSalPagados+salarioEmp
    c+=1
        
    if(salarioEmp>200000):
        empGananMas200000 +=1
        
    if(salarioEmp<50000 and categoriaEmp==3):
        empGanMen50000Cat3 +=1
        
    legajoEmp = int(input("Ingrese el legajo del empleado: "))

#-------------------------------------------------
# Resultados
#-------------------------------------------------
print(impTotSalPagados)
salarioProm=impTotSalPagados/c
print(salarioProm)

print(impTotSueldoCat1)
print(impTotSueldoCat2)
print(impTotSueldoCat3)

print(legajoMax, sueldoMax)
print(legajoMin, sueldoMin)

print(empGananMas200000)
print(empGanMen50000Cat3)


