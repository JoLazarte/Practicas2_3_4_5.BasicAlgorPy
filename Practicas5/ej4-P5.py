"""
-----------------------------------------------------------------------------------------------
Título: ejercicio 4
Fecha:
Autor:

Descripción:
Una empresa factura a sus clientes el último día de cada mes.
nroCliente = 333333
montoFactura = 22222
primeros10DiasMes = montoFactura - 200  or montoFactura - (2*montoFactura/100)
#si el 2% es > 200, se aplica ese -2%; si no, se descuenta 200
despues10DiasMes = montoFactura (HASTA EL DÍA 20)
despuesDia20 = montoFactura + 350 or montoFactura + (10*montoFactura/100)
#si el 10% es > 350 se aplica ese +10%; si no, se aumenta 350

Leer el número del cliente y el total de la factura
Emitir un informe donde conste el número del cliente y los tres importes que podría
abonar según la fecha de pago.

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
nroCliente = int(input("Ingrese número de cliente: "))
#-------------------------------------------------
# Procesos
#-------------------------------------------------
while nroCliente !=-1:
    montoFactura = float(input("Ingrese el monto que debe pagar: "))
    while (montoFactura < 1):
        montoFactura = float(input("Monto inválido. Ingrese el monto que debe pagar: "))

    descuentoA =  montoFactura - 200
    descuentoB = montoFactura - (2*montoFactura/100)
    if( descuentoA < descuentoB):
        primeros10DiasMes = descuentoB
    else:
        primeros10DiasMes = descuentoA
    print("Pagando los primeros 10 días del mes, tiene descuento del 2% o un reintegro de $200.")
    print(f"Como el monto de su factura es de {montoFactura} pesos, abonaría: {primeros10DiasMes} pesos.")
    
    print("Pagando después de los 10 días y antes de los 20 días del mes, abona el total de la factura, sin descuentos ni importes extra.")
    print(f"Deberá abonar entonces: {montoFactura} pesos.")
    
    inpuestoA =  montoFactura + 350
    inpuestoB = montoFactura + (10*montoFactura/100)
    if( inpuestoA < inpuestoB):
        despuesDia20 = inpuestoB
    else:
        despuesDia20 = inpuestoA
    print("Pagando después de los primeros 20 diás del mes, debe abonar un importe extra del 10% o un recargo de $350.")
    print(f"Como el monto de su factura es de {montoFactura} pesos, abonaría: {despuesDia20} pesos.")

    nroCliente = int(input("Ingrese número de cliente: "))

#-------------------------------------------------
# Resultados
#-------------------------------------------------


