"""
La sucesión de Fibonacci es una sucesión de números enteros donde cada término se obtiene como suma de los
dos anteriores, siendo los dos primeros 0 y 1: Fib(0)=0; Fib(1)=1
Por lo tanto, Fib=0, 1, 1, 2, 3, 5, 8, 13, 21....
Realizar un programa que lea N e imprima los N primeros términos de la sucesión Fib(N), como así también la suma de ellos.
"""
# EPS+CE

#Entrada: Se lee N

n=int(input("Ingrese nro de termino: "))

#PROC******************************************************************************
#para sumar los 2 terminos anteriores a n
aa=0  #primer termino  fib(0)
a=1   #segundo termino  fib(1)

if n > 1:  #siempre se va a imprimir el primer y segundo termino iniciales.
    print ("el primer término en la sucesión fibonacci es: ", aa)   #primer término
    print("el segundo término en la sucesión fibonacci es: ", a)     #segundo término
    #inicializar
    fb=0 #inicializo en 0 la suma fib de n
    for c in range(2,n+1): #La VUELTA SE INICIA 2, poque ya tengo FIB(0) y FIB(1), TERMINA en n+1, pra que ya no se calcule el término siguiente al ingresado.
        #Subproceso:
        fb=a+aa  # suma de los dos terminos anteriores. PRIMERA VUELTA fb(2)=1; SEGUNDA (SI n > 3), fb(3)=2; TERCERA, fb(4)=3
        print("Por el momento, la suma es : ", fb)
        #Defino los nuevos 2 ultimos terminos, para la 2da y siguientes:
        aa=a # lo que valia a ahora se guarda en aa, aa. 1ra VUELTA aa=1; SEGUNDA, aa=1; TERCERA, aa=2
        a=fb # nuevo valor de a = aa anterior + a anterior. 1ra VUELTA a=1; SEGUNDA, a=2; TERCERA, a=3
    
else: #si n es 0 o 1, la suma siempre será 0 o 1
    fb= aa + n
    print ("el primer término en la sucesión fibonacci es: ", aa)  #primer término
#FIN PROC *************************************************************************    
#Salida:    
print(f"La suma para el nro término {n} es: ",fb)

#*****OPCIÓN MÁS SIMPLE******************************************************************************
a1=1 #f(1)
a2=1 #f(2)
N=int(input("Ingrese nro: "))
f=-1
if N == 0:
    f=0
else:
    f=1 #cuando N=1 o N=2, f=0
    #En la primera vuelta, con N=2, se mantiene l valor de f=1, empieza a cambiar en la siguiente vuelta, despues de reasignar los valores de a1 y a2
    for i in range(2,N): #dara una vuelta menos a N, porque la suma f comienza en f(3)=f(1)+f(2)=2
        f=a1+a2
        a1,a2=a2,f
        
print(f)
