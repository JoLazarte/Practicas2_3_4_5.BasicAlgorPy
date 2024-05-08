def espar(valor):
    if valor%2==0:
        return 1
    else:
        return 0


# Programa principal
nro=int(input("Ingrese un valor: "))
result=espar(nro)
# evalua el resultado que devuelve la función
if result==1:
    print(" el valor ingresado es par")
else:
    print("El valor ingresado NO es par")

print ("fin")