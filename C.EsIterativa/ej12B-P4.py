def Fibonaci(n):
    a1=0 #f(0)
    a2=1 #f(1)
    f=0 #suma de los últimos términos para f(0)
    if N==1:
        f=1 #suma de los últimos términos para f(1)
    else:
        for i in range(2,n+1):#el bucle comienza en f(2), con f=1 y se detendrá en f(N+1), que no será incliudo.
            f=a1+a2 #suma de los últimos términos para f(N), desde f(2) hasta f(N)
            a1,a2=a2,f
    return f
    
N=int(input("Ingrese nro: "))

print(Fibonaci(N))
