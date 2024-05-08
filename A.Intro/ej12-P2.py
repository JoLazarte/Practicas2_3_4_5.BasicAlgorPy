"""
Escribir un programa para convertir un número binario de 4 cifras en un número decimal.
El número binario se ingresa como un solo número entero de cuatro dígitos.
Procedimiento:
Convertir un número binario a decimal: ---> multiplicar el valor de cada dígito
por 2^n. Este exponente se obtiene de la posición que ocupa el dígito dentro del número,
comenzando desde la derecha con la posición 0. Todos estos resultados se suman para
obtener el valor final. 
Ejemplo: Convertir 1011 a decimal:  1 * 2³ + 0 * 2² + 1 * 2¹ + 1 * 2༠ = 11

"""
nuBi1 = int (input ("Ingrese un número entero entre el 0 y el 1: "))
nuBi2 = int (input ("Ingrese un número entero entre el 0 y el 1: "))
nuBi3 = int (input ("Ingrese un número entero entre el 0 y el 1: "))
nuBi4 = int (input ("Ingrese un número entero entre el 0 y el 1: "))

numDec = nuBi1* 2**3 + nuBi2 * 2**2 + nuBi3 * 2**1 + nuBi4 * 2**0

print(numDec)