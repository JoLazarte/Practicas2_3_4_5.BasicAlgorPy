"""
Programa que imprima la suma de los números impares comprendidos entre 42 y 176.
"""
#Entrada
nroIn = 42 #43
nroFi = 176 #175

#Inicialización
c=43
sum=0

#Proceso C.E.

#par = False  
#for c in range (nroIn, nroFi+1):
    #par = not par
    #if par:
        #sum=sum+c
for c in range (nroIn+1,nroFi-1,2):    
    sum=sum+c

#Salida
print(sum)
