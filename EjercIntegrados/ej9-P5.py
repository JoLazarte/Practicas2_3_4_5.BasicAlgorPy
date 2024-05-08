"""
-----------------------------------------------------------------------------------------------
Título: ejercicio 9
Fecha:
Autor:

Descripción: 
Ingresar un número N y validar que sea positivo. Luego:
a. Mostrar los primeros números impares, hasta alcanzar el número ingresado.
b. Informar la suma de esos números impares.
Ejemplo:
· Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.
· Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.
· Si se ingresa -5, se debe pedir otro número

Pendientes:

-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#-------------------------------------------------
nro = int(input("Ingrese un nro positivo: "))
sumImp=0
#-------------------------------------------------
# Procesos
#-------------------------------------------------

if(nro%2==0 and nro>0):
    for i in range(nro-1,0,-2):
        print(i)
        sumImp=sumImp+i
elif(nro%2!=0 and nro>0):
    for i in range(nro,0,-2):
        print(i)
        sumImp=sumImp+i
else:
    print("El nro debe ser positivo")
#-------------------------------------------------
# Resultados
#-------------------------------------------------
print(sumImp)


