# precio base a las primeras 12 unidades
# -10% del precio base a todas las unidades a partir de la 13va hasta la centena
# -25% del precio base a todas las unidades por encima de las 100 (centena)
"""
Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio
base es 100. El cálculo resultante sería:
100 * 12 + 90 * 88 + 75 * 130 = 18870
y el precio promedio es de 18870/230 = 82.04
Programa que lea la cantidad solicitada de un producto y su precio base,
Valor total de la venta y el precio promedio por unidad.
El fin de carga se determina ingresando -1 como cantidad solicitada.
Al finalizar informar:
· Cantidad de ventas realizadas en total.
· Cantidad de ventas en las que se aplicó un 10% de descuento.
· Cantidad de ventas en las que SOLO se aplicó el precio base, es decir
que no se le realizaron descuentos.
"""
#Entrada
cantProducto=int(input("Ingrese cantidad solicitada: "))

valorTolVenta=0
precPromUnidad=0 #promedio por producto al aplicarle los descuentos

precBase12=0 #12*precio base
precDes10=0 # cantidad de 12 a 100 * ((10*precio de base)/100)
precDes25=0 # cantidad > 100 * ((25*precio de base)/100)

cont100Des10=0
contMas100Des10=0

ventasXprod10Desc=0
ventasXprodSoloPrecBase=0
cantTolVentasXproducto=0

#Proceso C.C.
while cantProducto != -1:
    precioBase=int(input("Ingrese el precio base: "))
    while (precioBase < 1):
        precioBase=int(input("Ingrese un precio base válido: "))
        
    if(cantProducto<=12):
        precBase12=precioBase * cantProducto
        precPromUnidad=precioBase
        ventasXprodSoloPrecBase=ventasXprodSoloPrecBase+1
        
        print("El valor total a abonar por el producto que no supera las 12 unidades es: ", precBase12)
        print("El precio promedio del producto, de ", cantProducto, " unidades es igual al del precio base: ", precPromUnidad)

    else:
        if(cantProducto>12 and cantProducto<=100):
            precBase12=precioBase * 12
            resto10Desc=cantProducto-12
            precDes10=(precioBase - ((precioBase * 10)/100)) * resto10Desc
                    
            valorTolVenta=precBase12+precDes10
            precPromUnidad=valorTolVenta/cantProducto
            
            cont100Des10=cont100Des10+1
            
            print("El valor a abonar por el total de las unidades del producto es: ", valorTolVenta)
            print("El precio promedio del producto, del total de las unidades es de: ", precPromUnidad)
            print("El precio base de las 12 primeras unidades del producto es: ", precBase12)
            print("A ", resto10Desc, " unidades del producto se le aplicó un descuento del 10%: ", precDes10)

        else:
            if(cantProducto>100):
                #los primeros 12
                precBase12=precioBase * 12

                #100-12=88 -> entre 13 y 100
                precDes10=(precioBase - ((precioBase * 10)/100)) * 88

                #los que se pasan de 100 en adelante
                resto25Desc=cantProducto-100
                precDes25=(precioBase - ((precioBase * 25)/100)) * resto25Desc
                
                valorTolVenta=precBase12+precDes10+precDes25
                precPromUnidad=valorTolVenta/cantProducto
                
                contMas100Des10=contMas100Des10+1
                
                print("El valor a abonar por el total de las unidades del producto es: ", valorTolVenta)
                print("El precio promedio del producto, del total de las unidades es de: ", precPromUnidad)
                print("El precio base de las 12 primeras unidades del producto es: ", precBase12)
                print("A 88 unidades del producto se le aplicó un descuento del 10%: ", precDes10)
                print("A ", resto25Desc, " unidades del producto se le aplicó un descuento del 25%: ", precDes25)

                
    cantTolVentasXproducto=cantTolVentasXproducto+1
    ventasXprod10Desc=cont100Des10+contMas100Des10

    cantProducto=int(input("Ingrese cantidad solicitada: "))

#Salida
print("Cantidad total de ventas por producto: ", cantTolVentasXproducto)
print("Ventas por producto con al menos 10% de descuento: ", ventasXprod10Desc)
print("Ventas por producto solo a precio de base: ", ventasXprodSoloPrecBase)

               
        


    
