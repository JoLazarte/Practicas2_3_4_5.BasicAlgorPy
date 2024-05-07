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
    print (aa)   #primer término
    print(a)     #segundo término
    #inicializar
    s=aa+a #el resultado siempre va a ser 1
    for c in range(3,n+1): #La VUELTA SE INICIA 3, PORQUE FIB(2) PUEDE CALCULARSE AL INICIO DEL "IF" (SI n ES 2, EL BUCLE NO SE INICIA, porque empieza en 3)
        #Subproceso:
        fb=a+aa  # suma de los dos terminos anteriores. PRIMERA VUELTA fb=1; SEGUNDA (SI n > 3), fb=2; TERCERA, fb=3
        print("Por el momento, la suma es : ", fb)
        #Defino los nuevos 2 ultimos terminos:
        aa=a    # lo que valia a ahora se guarda en aa, aa. 1ra VUELTA aa=1; SEGUNDA, aa=1; TERCERA, aa=2
        a=fb    # nuevo valor de a = aa anterior + a anterior. 1ra VUELTA a=1; SEGUNDA, a=2; TERCERA, a=3
        s+=fb #suma total actualizada: s anterior + fb actual. 1ra VUELTA: s=2; SEGUNDA: s=4 (s anterior = 2 + fb actual =2); TERCERA: s=7 (sAnterior=4+fbActual=3)
else: #si n es 0 o 1, la suma siempre será 0 y se imprime el unico valor anterior: 0
     s=0
     print (aa)
#FIN PROC *************************************************************************    
#Salida:    
print("La suma es ",s)
