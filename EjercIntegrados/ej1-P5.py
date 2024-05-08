#Leer números que representan edades de un grupo de personas hasta ingresar el -1
#Cuántos son menores de 18 años, promedio
#Cuántos tienen 18 años o más, promedio

#Se considera válida una edad entre 0 y 100

#Entrada
totalMen18=0
total18oMayor=0
sumMen18=0
sum18oMayor=0
persona=int(input("Ingrese nro de persona: "))

#Proceso C.C.
while persona !=-1:
    edad=int(input("Ingrese edad en nros: "))
    
    while (edad < 1 or edad > 100):
        edad=int(input("Ingrese edad en nros entre 1 y 100: "))
        
    if(edad<18):
        sumMen18=sumMen18+edad
        totalMen18=totalMen18+1
    else:
        sum18oMayor=sum18oMayor+edad
        total18oMayor=total18oMayor+1
     
    persona=int(input("Ingrese nro de persona: "))
 

#Salida
if (totalMen18>0):
    print("El promedio de menores de 18 años es: ", sumMen18/totalMen18)
if(total18oMayor>0):
    print("El promedio de mayores o iguales a 18 años es: ", sum18oMayor/total18oMayor)
