"""
-----------------------------------------------------------------------------------------------
Título: ejercicio 6
Fecha:
Autor:

Descripción: 
Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene. Tener
en cuenta que el número puede ser negativo. Ejemplo: Si se ingresa 12345 se debe imprimir 5.

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
nro = int(input("Ingrese número: "))
#-------------------------------------------------
# Procesos
#-------------------------------------------------
##---------SIN FUNCIÓN--------##
d = 0

while(nro != 0):
    nro = nro//10
    d += 1
print(d)

#Aqui nro ya vale cero, entonces no entraria en el while de la funcion, por eso se pideun nuevo valor para nro
##-----CON FUNCIÓN-------##
nro = int(input("Ingrese número: "))
def ContarDigitos(n):
    c = 0

    while(n != 0):
        n = n//10
        c += 1

    return c

#-------------------------------------------------
# Resultados
#-------------------------------------------------
print(ContarDigitos(nro))


