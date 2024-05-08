"""
Realizar un programa para ingresar desde el teclado un conjunto de números. Al
finalizar mostrar por pantalla el primer y último valor ingresado.
Finalizar la lectura con -1.

num = 0
nums = []
while num != -1:
    num= int(input("Ingrese un número: "))
    if num == -1:
        break
    #print(num)
    nums.append(num)

print(nums[0])
print(nums[len(nums)-1])
"""

numero= int(input("Ingrese un número: "))
primero = numero
while numero != -1:
    last = numero
    #print(last) 
    numero= int(input("Ingrese un número: "))
print(f"El primer número es {primero}, y el último número es {last}.")    