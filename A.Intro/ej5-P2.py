#Entrada

d1=int(input("Ingrese un número 1: "))
d2=int(input("Ingrese un número 2: "))
d3=int(input("Ingrese un número 3: "))

#Proceso

p1=d1*100/(d1+d2+d3)
p2=d2*100/(d1+d2+d3)
p3=d3*100/(d1+d2+d3)

#Salida

print("Porcentaje 1:", p1, "%")
print("Porcentaje 2:", p2, "%")
print("Porcentaje 3:", p3, "%")