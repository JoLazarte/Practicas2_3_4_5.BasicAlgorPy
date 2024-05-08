def Fibonaci(n):
    a1=0
    a2=1
    f=0
    for i in range(2,n+1):
        f=a1+a2
        a1,a2=a2,f
    return f
    

N=int(input("Ingrese nro: "))

print(Fibonaci(N))
