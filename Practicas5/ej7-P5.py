"""
-----------------------------------------------------------------------------------------------
Título: ejercicio 7
Fecha:
Autor:

Descripción: Leer un número entero e invertir las cifras que contiene. Imprimir por pantalla el
número invertido. Tener en cuenta que el número puede ser negativo. Por ejemplo, si se
ingresa 1234 debe mostrar 4321.

Pendientes:

-----------------------------------------------------------------------------------------------
"""
# Cuenta hasta que no hay mas digitos, es decir hasta que n//10 = 0
def ContarDigitos(n):
    c = 0

    while(n != 0):
        n = n//10
        c += 1

    return c

def invertirNumero(n):
    cantidadDeDigitos = ContarDigitos(n) #obtengo el "largo" del nro
    nroInvertido = 0 #se ira formando el nro invertido

    for x in range(cantidadDeDigitos - 1, -1, -1): #el ciclo comenzara en x = ["largo" del nro -1], ira decreciendo de a uno [-1], hasta llegar a x = 0 [debido al -1]
        nroInvertido += (n % 10) * 10 ** x #el resto del nro (que se va achicando) div 10 se multiplica por 10 a la potencia del valor que vaya tomando x. El resultado se suma al resultado de la anterior vuelta
        n //= 10 #el nro se va achicando en "largo"
        #print(nroInvertido)
    return nroInvertido

#Entrada
nro=int(input("Ingrese un numero: "))
#Salida
print("nro invertido:", invertirNumero(nro))
