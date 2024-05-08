"""
Realizar un programa que lea un número natural H e imprima un mensaje indicando si H es primo o no.
Se dice que un número es primo cuando sólo es divisible por sí mismo y por la unidad.
"""
# EPS+CC

#Entrada
n=int(input("Ingrese nro: "))
#Proc************************
#inicializacion
primo=True
c=2 #todo num es divisible por 1 (la unidad), pero si ya es divisible por 2, entonces ya no es primo
while primo and c < n : #la cant de vueltas del bucle estrá entre c=2 y n; se toma la bandera "primo=True" como punto de partida, ya que inicialmente todo num es divisible por 1 (la unidad)
    #Subproceso:
    if n % c==0: #si en la primera vuelta, el num n ingresado ya es divisible por c=2, NO es primo; si el resto no da 0, se sigue preguntando hasta llegar a dividir n por n.
        primo=False        
    c+=1
#Fin del Proc ***************   
#Salida:    
if primo:
    cartel="Primo"
else:
    cartel="No primo"
print (cartel)