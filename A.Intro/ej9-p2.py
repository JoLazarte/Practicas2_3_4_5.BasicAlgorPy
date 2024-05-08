"""
Una inmobiliaria paga a sus vendedores un salario de $50000, más una comisión de $5000
por cada venta realizada, más el 5% del valor de las ventas. Realizar un programa que
imprima el número del vendedor y el salario que le corresponde en un determinado mes.
Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las
mismas. 

"""
NroVen = int (input ("Ingrese el nro de vendedor: "))

NVent = int (input ("Ingrese la cant de ventas que realizó el vendedor: "))

TVent = int (input ("Ingrese el precio total de las ventas: "))

Sal=50000 + NVent * 5000 + TVent * 0.05

print(Sal)